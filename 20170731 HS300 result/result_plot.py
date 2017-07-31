import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt


data = pd.read_csv('hs300 profit.csv',encoding='utf8',index_col='datetime',parse_dates=True)

data = data.dropna(axis=0,how='any')
data = data.reset_index(drop=True)
index = data.index
profit_per_share = data.profit
profit_without_fee = data.profit_without_fee
profit_with_fee = data.profit_with_fee

fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(2,1,1)
ax1.bar(index, profit_per_share,width=0.5,label='profit_per_share')
for x, y in zip(index,profit_per_share):
    ax1.text(x, y, '%.2f' % y, ha = 'center', va = 'bottom')
plt.legend()


ax2 = fig.add_subplot(2,1,2)
ax2.bar(index,profit_without_fee,width=0.5,label='profit_without_fee',color='g')
ax2.bar(index,profit_with_fee,width=0.5,label='profit_with_fee',alpha=0.5,color='r')
# for x,y in zip(index,profit_with_fee):
#     ax2.text(x, y, '%.2f' % y, ha = 'center', va = 'bottom')


plt.legend()

plt.show()