# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:31:09 2022

@author: User
"""

import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib

startTime = '2018-01-01'
endTime = '2021-12-31'
df_2330 = pdr.DataReader('2330.TW', 'yahoo', startTime, endTime)

prices1 = list(filter(None, df_2330['Close']))
plt.plot(prices1, 'r-', label="收盤價")
plt.show()

print(df_2330['Close'])