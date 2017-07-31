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
    logger.info("RunInfo: {}".format(context.run_info))
    scheduler.run_daily(update)
    context.count = 0


# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    pass


# 你选择的期货数据更新将会触发此段逻辑，例如日线或分钟线更新
def handle_bar(context, bar_dict):
    # 开始编写你的主要的算法逻辑
    # bar_dict[order_book_id] 可以获取到当前期货合约的bar信息
    # context.portfolio 可以获取到当前投资组合信息
    # 使用buy_open(id_or_ins, amount)方法进行买入开仓操作
    if context.count % 60 == 0:
        hourly(context, bar_dict)
    else:
        pass
    context.count = (context.count + 1) % 60
    '''
    hourly(context,bar_dict)
    '''


# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    pass


def update(context, bar_dict):
    context.future = get_dominant_future(context.s1)
    update_universe(context.future)


def how_many(context, bar_dict):
    ins = instruments(context.future)
    rate = ins.margin_rate
    # return context.amount // (bar_dict[context.future].close * rate)
    logger.info('账户资金:{}'.format(context.portfolio.cash))
    logger.info('future_account可用资金:{}'.format(context.future_account.cash))
    logger.info('价格:{}'.format(bar_dict[context.future].close))
    # logger.info('开仓手数:{}'.format(context.portfolio.cash // bar_dict[context.future].close))
    return context.future_account.cash // bar_dict[context.future].close


def hourly(context, bar_dict):
    position = context.portfolio.positions[context.future]
    hold_sell = position.sell_quantity
    hold_buy = position.buy_quantity
    prices = history_bars(context.future, 30, frequency='60m', fields=['high', 'low', 'close'])
    high = prices['high']
    low = prices['low']
    close = prices['close']
    ma21 = talib.MA(close, timeperiod=21)
    slowk, slowd = talib.STOCH(high, low, close,
                               fastk_period=9,
                               slowk_period=3,
                               slowk_matype=0,
                               slowd_period=3,
                               slowd_matype=0)
    if hold_buy == 0 and hold_sell == 0:
        if close[-2] > ma21[-2] and slowk[-2] < slowd[-2] and close[-1] > ma21[-1] and slowk[-1] > slowd[-1]:
            number = how_many(context, bar_dict)
            buy_open(context.future, amount=number)
            stop = np.max(close)
            context.stop = stop
            logger.info('买入开仓{}手,止盈价格{}'.format(number, stop))
        elif close[-2] < ma21[-2] and slowk[-2] > slowd[-2] and close[-1] < ma21[-1] and slowk[-1] < slowd[-1]:
            number = how_many(context, bar_dict)
            sell_open(context.future, amount=number)
            stop = np.min(close)
            context.stop = stop
            logger.info('卖出开仓{}手,止盈价格{}'.format(number, stop))
        else:
            pass
    elif hold_buy > 0:
        if close[-1] >= context.stop:
            sell_close(context.future, hold_buy)
            logger.info('价格达到止盈价格，平多仓')
        elif close[-1] < ma21[-1]:
            sell_close(context.future, hold_buy)
            logger.info('价格低于21日均线，平多仓')
        else:
            pass
    elif hold_sell > 0:
        if close[-1] <= context.stop:
            buy_close(context.future, hold_sell)
            logger.info('价格低于止盈价格，平空仓')
        elif close[-1] > ma21[-1]:
            buy_close(context.future, hold_sell)
            logger.info('价格高于21日均线，平空仓')
        else:
            pass
    else:
        pass
    plot('close', bar_dict[context.future].close)