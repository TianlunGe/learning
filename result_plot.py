import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame


data = pd.read_csv('profit.csv',index_col=0)[150:]
data=data.dropna(axis=0,how='any')
print(data)
fig = plt.figure(figsize=(9,6))
# ax = fig.add_subplot(1,1,1)
# data.plot(kind='bar')
index = data.index
y1 = data['expect_profit']
y2 = data['real_profit']
side = data['side']
plt.bar(index,y1,label='expect_profit')
plt.bar(index,y2,alpha=0.5,label='real_profit')

for x,y,side in zip(index, y1, side):
    plt.text(x,y,'%i %s' % (y,side[0]), ha = 'center', va = 'bottom')

for x,y in zip(index, y2):
    plt.text(x, y+10, '%i' %y, ha = 'center', va = 'bottom')

plt.legend()
plt.show()
