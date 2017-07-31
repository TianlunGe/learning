import numpy as np
import talib
import datetime


# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    # 在context中保存全局变量
    context.s1 = "399300.XSHE"
    # 实时打印日志
    logger.info("RunInfo: {}".format(context.run_info))
    context.amount = 100000
    scheduler.run_daily(daily_work, time_rule=market_close(minute=5))


# before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
def before_trading(context):
    pass


# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    pass


# after_trading函数会在每天交易结束后被调用，当天只会被调用一次
def after_trading(context):
    pass


def daily_work(context, bar_dict):
    stock = context.s1
    prices = history_bars(stock, 30, frequency='1d', fields=['high', 'low', 'close'])
    high = prices['high']
    low = prices['low']
    close = prices['close']
    ma21 = talib.MA(close, timeperiod=21)
    stop = np.max(close)
    slowk, slowd = talib.STOCH(high, low, close,
                               fastk_period=9,
                               slowk_period=3,
                               slowk_matype=0,
                               slowd_period=3,
                               slowd_matype=0)
    # if close[-2] > ma21[-2] and slowk[-2] < slowd[-2] and close[-1] > ma21[-1] and slowk[-1] > slowd[-1]:
    #     logger.info('{} buy stock'.format(context.now))
    stock_hold = context.portfolio.positions[stock].quantity
    if stock_hold > 0:
        logger.info('当前持有 {0} 数量:{1}'.format(stock, stock_hold))
        if close[-1] < ma21[-1]:
            logger.info('当前收盘价{0}低于21日均线价格{1},卖出'.format(close[-1], ma21[-1]))
            order_shares(stock, -1 * stock_hold)
        elif close[-1] >= stop:
            logger.info('收盘价{0}高于30内最高价{1},卖出'.format(close[-1], stop))
            order_shares(stock, -1 * stock_hold)
    else:
        if close[-2] > ma21[-2] and slowk[-2] < slowd[-2] and close[-1] > ma21[-1] and slowk[-1] > slowd[-1]:
            logger.info('买入{0}价格{1}'.format(stock, context.amount))
            order_value(stock, context.amount)
        else:
            pass
    plot('close', close[-1])
















