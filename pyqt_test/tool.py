from datetime import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from WindPy import *
import scipy
from scipy import stats
from scipy.stats import mode
from numpy import nan

# #########start############

# '''
# #获取时间长度、终止时间和时间间隔,名称
# def get_timelength_end_interval():
#  name=input('请输入所取股票或期货名称(形如：600000.SH)：')
#     interval=int(input('请选择时间间隔：{1：tick   2:分钟   3：日}:'))
#     if interval==1 or interval==2:
#         timelength=input('请输入需要查询的时间长度：{1:日   2：周   3：月   4：半年   5：1年   6:5年}')
#         end=input('请输入终止时间(形如：2017-01-01 09:00:00),按enter键默认当前时间：')
#         if end=='':
#             end=datetime.now()
#     elif interval==3 or interval==4 or interval==5 or interval==6 or interval==7 or interval==8:
#         timelength=input('请输入需要查询的时间长度：{1:日   2：周   3：月   4：半年   5：1年   6:5年}')
#         end=input('请输入终止时间(形如：2017-01-01),按enter键默认当前时间：')
#         if end=='':
#             end=datetime.today()
#     else:
#         print('InputError!')
#         get_timelength_end_interval()
#     return name,timelength,end,interval
#
# #计算开始时间
# def get_start(timelength,end):
#     if timelength==1:
#         start=end-timedelta(1)
#     elif timelength==2:
#         start=end-timedelta(7)
#     elif timelength==3:
#         start=end-timedelta(31)
#     elif timelength==4:
#         start=end-timedelta(183)
#     elif timelength==5:
#         start=end-timedelta(365)
#     elif timelength==6:
#         start=end-timedelta(1825)
#     return start
#
# #Get获取数据的域
# def get_fields():
#     f=[]
#     fields=input('请输入需要获取的数据域：{1：open   2：high   3：low   4:close},可选择多项（形如：134）:')
#     if '1' in fields:
#         f.append('open')
#     if '2' in fields:
#         f.append('high')
#     if '3' in fields:
#         f.append('low')
#     if '4' in fields:
#         f.append('close')
#     return f
# '''
# #均值填充
def addmean(data):
   sum=0
   count=0
   for j in range(len(data)):
      if data[j]==nan:
         pass
      else:
         sum+=data[j]
         count+=1
   mean=sum/count
   for k in range(len(data)):
      if data[k]==nan:
         data[k]=mean
   return data
#获取数据
def getdata(name,fields,start,end,period,interval):
   if not w.isconnected():
      w.start()
   if interval:
      data=w.wsd(name,fields,start,end,Period=period)
   else:
      data=w.wsi(name,fields,start,end,BarSize=period)
   ####判断获取数据是否出错#####
   return data


#统计值获取
def get_MeasureIndex(d):
   mean, Median, Mode, Quartiles, Minimum, Maximum, Range, variance, sd, cv,skewness,kurtosis = [], [], [], [], [], [], [], [], [], [],[],[]
   column = ['mean', 'median', 'mode', 'quartiles', 'min', 'max', 'range', 'variance', 'sd',
           'Coefficient of Variation','kewness','kurtosis']
   measure = pd.DataFrame(np.zeros([len(column),len(d.columns)]), index=column, columns=d.columns)
   for i in range(len(d.columns)):
      mean.append(d.iloc[:,i].mean())
      Median.append(d.iloc[:,i].median())
      Mode.append(d.iloc[:,i].mode())
      Quartiles.append(d.iloc[:,i].quantile(0.25))
      Minimum.append(d.iloc[:,i].min())
      Maximum.append(d.iloc[:,i].max())
      Range.append(d.iloc[:, i].max() - d.iloc[:, i].min())
      variance.append(d.iloc[:, i].var())
      sd.append(d.iloc[:, i].std())
      cv.append(d.iloc[:, i].mean() / d.iloc[:, i].std())
      skewness.append(d.iloc[:, i].skew())
      kurtosis.append(d.iloc[:, i].kurt())
   measure.iloc[0]=mean
   measure.iloc[1] = Median
   measure.iloc[2] = Mode
   measure.iloc[3] = Quartiles
   measure.iloc[4] = Minimum
   measure.iloc[5] = Maximum
   measure.iloc[6] = Range
   measure.iloc[7] = variance
   measure.iloc[8] = sd
   measure.iloc[9] = cv
   measure.iloc[10]=skewness
   measure.iloc[11]=kurtosis
   return measure


'''
#获取variability指数
def get_Variability(d):
   Range=[]
   variance=[]
   sd=[]
   cv=[]
   for i in range(len(d.columns)):
      Range.append([d.iloc[:,i].min(),d.iloc[:,i].max()])
      variance.append(d.iloc[:,i].var())
      sd.append(d.iloc[:,i].std())
      cv.append(d.iloc[:,i].mean() /d.iloc[:,i].std())
   return Range,variance,sd,cv
'''
#获取峰度、偏度和正态性测试结果
def GetIndex(s,index1,index2,index3,Y_or_N,i):
      index1.append(stats.shapiro(s))
      index2.append(stats.kstest(s,'norm'))
      index3.append(stats.normaltest(s))
      if index1[i][1]>=0.05 or index2[i][1]>=0.05 or index3[i][1]>=0.05:
         Y_or_N.append(1)
      else:
         Y_or_N.append(0)

#判断是否满足正态性,进行box-cox变换
def judge(d,Y_or_N,i,flag):
   if Y_or_N[i]==0:            #表示不满足正态分布，需要进行box-cox处理
      d1=stats.boxcox(d.iloc[:,i])
      d11=np.array(d1[0])
      flag.append(1)
   else:
      flag.append(0)
      d11=np.array(d.iloc[:,i])
   return d11

#绘制直方图
def drawHist(values,fields,mean,sd,ax1):
   # ax1 = fig.add_subplot(1, 3, 1)
   n,bins,patches=ax1.hist(values, 70, facecolor='green')
   ax1.set_xlabel(fields)
   ax1.set_ylabel('Frequency')
   ax1.set_title(fields+' distribution Hist')
   mu=mean
   sigma=sd
   y=mlab.normpdf(bins,mu,sigma)
   ax1.plot(bins,y,'r--',linewidth=1)
   # plt.show()
   return bins,y

#绘制Q-Q PLOT
def drawQQplot(s,ax2):
   # ax2 = fig.add_subplot(1, 3, 2)
   stats.probplot(s, dist="norm", plot=ax2)
   ax2.set_title("Normal Q-Q plot")
   # plt.show()

#绘制mu-sigma图
def drawplot(values,field,mu,sigma,bins,y,ax3,flag):
   #plt.subplot(133)
   #ax3 = fig.add_subplot(1, 3, 3)
   if flag==1:
      ax3.set_title(field+',data has been box-cox')
   else:
      ax3.set_title(field+',data has not been box-cox')
   ax3.axis([min(bins), max(bins), min(y), max(y)])
   #ax3.plot(bins,y,'r--',linewidth=1)
   #bins, y = drawHist(values, d.columns[i], mu,sigma, ax3)
   #ax3.vlines((mu-4*sigma,mu-3*sigma,mu-2*sigma,mu-sigma,mu,mu+sigma,mu+2*sigma,mu+3*sigma,mu+4*sigma),min(y),max(y))
   # ax3.text((mu-4*sigma,mu-3*sigma,mu-2*sigma,mu-sigma,mu,mu+sigma,mu+2*sigma,mu+3*sigma,mu+4*sigma),-1,('μ-4σ','μ-3σ','μ-2σ','μ-σ','μ','μ+σ','μ+2σ','μ+3σ','μ+4σ'))
   ax3.vlines(mu, min(y), max(y))
   ax3.text(mu, min(y)-0.8, r'$μ-σ$')
   for i in range(1, int((mu - min(values)) // sigma) + 1, 1):
      ax3.vlines(mu - i * sigma, min(y), max(y))
      ax3.text(mu - i * sigma, min(y)-0.8,r'$μ-%sσ$' %i)
   for i in range(1, int((max(values) - mu) // sigma) + 1, 1):
      ax3.vlines(mu + i * sigma, min(y), max(y))
      ax3.text(mu + i * sigma, min(y)-0.8, r'$μ+%sσ$' %i)


####绘制mu-sigma图,将指定值在图中标注
def drawplot_with_specialtarget(values,field,mu,sigma,bins,y,specialtarget,ax3,flag):
   #plt.subplot(133)
   #ax3 = fig.add_subplot(1, 3, 3)
   if flag==1:
      ax3.set_title(field+',data has been box-cox')
   else:
      ax3.set_title(field+',data has not been box-cox')
   ax3.axis([min(bins), max(bins), min(y), max(y)])
   #ax3.plot(bins,y,'r--',linewidth=1)
   #bins, y = drawHist(values, d.columns[i], muu, sigma, ax3)
   #ax3.vlines((mu-4*sigma,mu-3*sigma,mu-2*sigma,mu-sigma,mu,mu+sigma,mu+2*sigma,mu+3*sigma,mu+4*sigma),min(y),max(y))
   #ax3.text((mu-4*sigma,mu-3*sigma,mu-2*sigma,mu-sigma,mu,mu+sigma,mu+2*sigma,mu+3*sigma,mu+4*sigma),-1,('μ-4σ','μ-3σ','μ-2σ','μ-σ','μ','μ+σ','μ+2σ','μ+3σ','μ+4σ'))
   ax3.vlines(mu , min(y), max(y))
   ax3.text(mu-0.3, min(y) - 0.8, r'$μ-σ$')
   for i in range(1, int((mu - min(values)) // sigma) + 1, 1):
      ax3.vlines(mu - i * sigma , min(y), max(y))
      ax3.text(mu - i * sigma-0.3, min(y) - 0.8, r'$μ-%sσ$' % i)
   for i in range(1, int((max(values) - mu) // sigma) + 1, 1):
      ax3.vlines(mu + i * sigma, min(y), max(y))
      ax3.text(mu + i * sigma-0.3, min(y) - 0.8, r'$μ+%sσ$' % i)
   ax3.vlines(specialtarget,min(y),max(y))
   s=(specialtarget-mu)/sigma
   ax3.text(specialtarget-0.3, max(y)-1, r'$μ%sσ$' % s)
'''
#normal test#是否满足正态性，若不满足进行box-cox变换，再次判断，若满足正态性，画图
def Distribution_test(d,flag):
   d11=[]
   index1,index11 = [],[]  # 获取shapiro返回的指标
   index2,index22 = [],[]  # 获取kstest返回的指标
   index3,index33 = [],[]  # 获取snormaltest返回的指标
   Y_or_N ,Y_or_N_NEW= [],[]  # 判断是否符合正态分布
   for i in range(len(d.columns)):
      GetIndex(d.iloc[:,i],index1,index2,index3,Y_or_N,i)
   for i in range(len(d.columns)):
      judge(d,Y_or_N,i,d11,flag)
   d11 = np.array(d11)
   d11 = d11.T
   d_new = pd.DataFrame(d11, index=d.index, columns=d.columns)
   ######若数据被标记已经经过box-cox变换，重新判断是否满足正态性######
   for i in range(len(d.columns)):
      if flag[i]==1:
         GetIndex(d_new.iloc[:,i],index11,index22,index33,Y_or_N_NEW,i)
      else:
         index11.append(index1[i])
         index22.append(index2[i])
         index33.append(index3[i])
         Y_or_N_NEW.append(Y_or_N[i])
   return d_new,Y_or_N_NEW
'''

#####第三幅图####
def thirdpicture(d,d_new,Y_or_N_NEW,bins,y,i,fig,flag,specialtarget):
      if Y_or_N_NEW[i]==1 and specialtarget==None:
         drawplot(d_new.iloc[:,0],d.columns[i],d_new.iloc[:,0].mean(),d_new.iloc[:,0].std(), bins, y, fig,flag[i])
      elif Y_or_N_NEW[i]==1 and specialtarget!=None:
         drawplot_with_specialtarget(d_new.iloc[:,0],d.columns[i],d_new.iloc[:,0].mean(),d_new.iloc[:,0].std(), bins, y, specialtarget, fig,flag[i])
      else:
         plt.title(' ')
         plt.text(min(bins),(max(y)-min(y))/4,'Does not satisfy the normal distribution')
      # normal test#是否满足正态性，若不满足进行box-cox变换，再次判断，若满足正态性，画图


#全三幅图
def draw(d,i,flag,index1,index11,index2,index22,index3,index33,Y_or_N,Y_or_N_NEW,specialtarget=None):
   # fig.append(plt.figure())
   fig = plt.figure()
   #####数据未经过boxcox处理，画直方图、QQplot
   bins, y = drawHist(d.iloc[:, i], d.columns[i], d.iloc[:, i].mean(), d.iloc[:, i].std(),fig.add_subplot(1,3,1))
   drawQQplot(d.iloc[:, i],fig.add_subplot(1,3,2))
   #####数据经过box-cox处理#####
   d_new=Distribution_test(d, i,flag,index1,index11,index2,index22,index3,index33,Y_or_N,Y_or_N_NEW)
   ax3=fig.add_subplot(1,3,3)
   #ax3.axis([min(bins), max(bins), min(y), max(y)])
   bins, y = drawHist(d_new, d.columns[i], d_new.iloc[:, i].mean(), d_new.iloc[:, i].std(),ax3)
   thirdpicture(d,d_new, Y_or_N_NEW, bins, y, i, fig.add_subplot(1,3,3),flag,specialtarget)
   plt.show()
   # plt.show()
   print(0)
   #print(type(bins)+min(bins)+','+max(bins)+','+min(y)+','+max(y)+type(y))

def Distribution_test(d, i,flag,index1,index11,index2,index22,index3,index33,Y_or_N,Y_or_N_NEW):
   GetIndex(d.iloc[:, i], index1, index2, index3, Y_or_N, i)
   d11=judge(d, Y_or_N, i, flag)
   d11 = d11.T
   d_new = pd.DataFrame(d11, index=d.index)
   ######若数据被标记已经经过box-cox变换，重新判断是否满足正态性######
   if flag[i] == 1:
      GetIndex(d_new.iloc[:, 0], index11, index22, index33, Y_or_N_NEW, i)
   else:
      index11.append(index1[i])
      index22.append(index2[i])
      index33.append(index3[i])
      Y_or_N_NEW.append(Y_or_N[i])
   return d_new

w.start()
data=w.wsi('600000.SH',('close','open'),'2017-06-01 09:00:00')
d=pd.DataFrame(data.Data)
d=d.T
d.index=data.Times
d.columns=data.Fields
flag = []  # 判断是否经过boxcox变换
index1, index11 = [], []  # 获取shapiro返回的指标
index2, index22 = [], []  # 获取kstest返回的指标
index3, index33 = [], []  # 获取snormaltest返回的指标
Y_or_N, Y_or_N_NEW = [], []  # 判断是否符合正态分布
draw(d,0,flag,index1,index11,index2,index22,index3,index33,Y_or_N,Y_or_N_NEW,specialtarget=None)

##########变换后的曲线######x