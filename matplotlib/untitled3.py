# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 16:12:00 2022

@author: User
"""
import matplotlib.pyplot as plt
import matplotlib
myfont = matplotlib.font_manager.FontProperties(
            fname='C:\Windows\Fonts\mingliu.ttc')

import pandas_datareader as pdr
import datetime as datetime


start = datetime.datetime(2016,1,5)
df_2330 = pdr.DataReader('2330.TW', 'yahoo', start=start)
df_2492 = pdr.DataReader('6547.TWO', 'yahoo', start=start)

plt.title("股價走勢圖", fontproperties=myfont, fontsize = 20)
plt.plot(df_2330['Adj Close'], 'r-', label="台積電")
plt.plot(df_2492['Adj Close'], 'b-', label="高端疫苗")
plt.legend(prop=myfont)
plt.show()
