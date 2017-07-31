import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame


data = pd.read_csv('profit.csv',index_col=0)

print(len(data[data.real_profit > 0]))
print(len(data[data.real_profit < 0]))
print(len(data[data.real_profit == 0]))