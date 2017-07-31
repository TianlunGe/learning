# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。
import talib
import numpy as np


# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    # context内引入全局变量s1
    context.s1 = "CU"
    # context.amount = 1000000
    # 初始化时订阅合约行情。订阅之后的合约行情会在handle_bar中进行更新。
    # subscribe(context.s1)
    # 实时打印日志
    update(context, None)
    context.hold = context.future
    logger.info("RunInfo: {}".format(context.run_info))
    context.count = 0
    context.win = 0
    context.loss = 0
    context.trade_fee = 0.000025
    scheduler.run_daily(update)
    scheduler.run_monthly(win_rate_log, tradingday=1)


# 你选择的期货数据更新将会触发此段逻辑，例如日线或分钟线更新
def handle_bar(context, bar_dict):
    if context.count % 60 == 0:
        hourly(context, bar_dict)
    else:
        pass
    context.count = (context.count + 1) % 60
    '''
    hourly(context,bar_dict)
    '''


# handle_bar实际操作，每小时运行一次
def hourly(context, bar_dict):
    # 查看当前是否仓位
    position = context.portfolio.positions[context.hold]
    hold_sell = position.sell_quantity
    hold_buy = position.buy_quantity
    # 获取主力合约200小时内数据
    prices = history_bars(context.future, 200, frequency='60m', fields=['high', 'low', 'close', 'open'])
    high = prices['high']
    low = prices['low']
    close = prices['close']
    # 当前持有合约数据，用来止损
    hold_close = history_bars(context.hold, 30, frequency='60m', fields='close')

    # 如果当前没有仓判断是否要开仓
    if hold_buy == 0 and hold_sell == 0:
        # 算ma21以及kd(9,3,3)
        ma21 = talib.MA(close, timeperiod=21)
        slowk, slowd = talib.STOCH(high, low, close,
                                   fastk_period=9,
                                   slowk_period=3,
                                   slowk_matype=0,
                                   slowd_period=3,
                                   slowd_matype=0)
        # 判断是否达到开条件
        if long_judge(prices, ma21, slowk, slowd):
            number = how_many(context, bar_dict)
            stop = np.max(close)
            context.stop = stop
            # 日志记录
            if stop < bar_dict[context.future].close:
                logger.error('当前价格{}已经大于止盈价格{}，不进行开仓操作'.format(bar_dict[context.future].close, stop))
            else:
                buy_open(context.future, amount=number)
                context.hold = context.future
                logger.info('买入开仓{}手,止盈价格{}'.format(number, stop))
        elif short_judge(prices, ma21, slowk, slowd):
            number = how_many(context, bar_dict)
            stop = np.min(close)
            context.stop = stop
            # 日志记录
            if stop > bar_dict[context.future].close:
                logger.error('当前价格{}已经小于止盈价格{}，不进行开仓操作'.format(bar_dict[context.future].close, stop))
            else:
                sell_open(context.future, amount=number)
                context.hold = context.future
                logger.info('卖出开仓{}手,止盈价格{}'.format(number, stop))
        else:
            pass
    elif hold_buy > 0:
        # 多头平仓判断
        hold_ma21 = talib.MA(hold_close, timeperiod=21)
        if close[-1] >= context.stop:
            logger.info('价格达到止盈价格，平多仓')
            sell_close(context.hold, hold_buy)
            context.win = context.win + 1
        elif close[-1] < hold_ma21[-1]:
            logger.info('价格低于21日均线，平多仓')
            sell_close(context.hold, hold_buy)
            context.loss = context.loss + 1
        else:
            pass
    elif hold_sell > 0:
        # 空头平仓判断
        hold_ma21 = talib.MA(hold_close, timeperiod=21)
        if close[-1] <= context.stop:
            logger.info('价格低于止盈价格，平空仓')
            buy_close(context.hold, hold_sell)
            context.win = context.win + 1
        elif close[-1] > hold_ma21[-1]:
            logger.info('价格高于21日均线，平空仓')
            buy_close(context.hold, hold_sell)
            context.loss = context.loss + 1
        else:
            pass
    else:
        pass
    plot('close', bar_dict[context.future].close)


# 多头开仓条件判断
def long_judge(prices, ma21, k, d):
    high = prices['high']
    low = prices['low']
    close = prices['close']
    open = prices['open']
    return low[-2] > ma21[-2] and close[-2] > open[-2] and k[-2] < d[-2] and low[-1] > ma21[-1] and close[-1] > open[
        -1] and k[-1] > d[-1]


# 空头开仓条件判断
def short_judge(prices, ma21, k, d):
    high = prices['high']
    low = prices['low']
    close = prices['close']
    open = prices['open']
    return high[-2] < ma21[-2] and close[-2] < open[-2] and k[-2] > d[-2] and high[-1] < ma21[-1] and close[-1] < open[
        -1] and k[-1] < d[-1]


# 计算满仓仓位
def how_many(context, bar_dict):
    ins = instruments(context.future)
    rate = ins.margin_rate
    multi = ins.contract_multiplier
    # logger.info('价格:{}'.format(bar_dict[context.future].close))
    # logger.info('开仓手数:{}'.format(context.portfolio.cash // bar_dict[context.future].close))
    per = bar_dict[context.future].close * multi * rate
    fee = bar_dict[context.future].close * multi * context.trade_fee
    logger.info('每份合约有{}份，保证金比率{}，每手合约需保证金{}'.format(multi, rate, per))
    logger.info('每手合约交易费用{}'.format(fee))
    return context.future_account.cash // (per + fee)


# 每天更新主力合约
def update(context, bar_dict):
    context.future = get_dominant_future(context.s1)
    # update_universe(context.future)
    subscribe(context.future)


def win_rate_log(context, bar_dict):
    logger.info('总计盈利次数{}'.format(context.win))
    logger.info('总计亏损次数{}'.format(context.loss))
    logger.info('未成交订单:{}'.format(get_open_orders()))


# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    pass


# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    pass