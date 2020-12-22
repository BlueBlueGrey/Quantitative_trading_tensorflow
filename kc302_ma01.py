# -*- coding: utf-8 -*-
'''
TopQuant-简称TQ极宽智能量化回溯分析系统，培训课件-配套教学python课件程序

Top极宽量化(原zw量化)，Python量化第一品牌 
by Top极宽·量化开源团队 2017.10.1 首发

网站： www.TopQuant.vip      www.ziwang.com
QQ群: Top极宽量化1群，124134140
      Top极宽量化2群，650924099
      Top极宽量化3群，450853713
  
'''

import os
import numpy as np
import pandas as pd
import tushare as ts

#  TopQuant
import zsys 
import zpd_talib as zta
import ztools_datadown as zddown
import ztools_draw as zdr

#----------

#1 读取数据
fss='data/600663.csv'
print('\nfss',fss)
df=pd.read_csv(fss,index_col=0)
df=df.sort_index(ascending=True);
print(df.tail())

#2 计算avg均值数据
df['avg']=df[zsys.ohlcLst].mean(axis=1).round(2)
print('\n#2,df')
print(df.tail())

#3
#. 
df2=zta.mul_talib(zta.MA,df, ksgn='avg',vlst=zsys.ma100Lst_var)
print('\n#3,ma_lst,',zsys.ma100Lst_var)
print('\ndf2.head')
print(df2.head())
print('\ndf2.tail')
print(df2.tail())



#4 绘制价格曲线图
hdr,fss='价格曲线图-ma均线','tmp/tmp_.html'
print('\n#4 fss,',fss)
vlst=list(map(lambda x:'ma_'+str(x), zsys.ma100Lst_var))
print('vlst,',vlst)
xlst=['avg']+vlst
print('xlst,',xlst)
df3=df2.tail(60)
zdr.drDF_mul_xline(df3,fss,m_title=hdr,xlst=xlst)



