text = '每份合约有5.0份，保证金比率0.05，每手合约需保证金8977.5	'
print(text.find('止盈价格'))
print(text[text.find('止盈价格')+4:])

def get_price(log):
    idx = log.find('止盈价格')
    if idx < 0:
        return None
    return log[idx+4:]


print(get_price('卖出开仓111.0手,止盈价格35790.0'))

s = 'SELL_OPEN'
s.en