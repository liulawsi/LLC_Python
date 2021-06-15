# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:33:05 2021

@author: User
"""

import twstock
import matplotlib.pyplot as plt
import matplotlib
myFont = matplotlib.font_manager.FontProperties(
            fname='C:\Windows\Fonts\mingliu.ttc')

plt.title("高端疫苗", fontproperties=myFont, fontsize = 20)

stock6547 = twstock.Stock("6547")
stock6547.fetch_from(2020, 1)

prices1 = list(filter(None, stock6547.price))
avg = stock6547.moving_average(prices1, 30)
prices2 =prices1[len(prices1)-len(avg):]

plt.plot(prices2, 'r-', label="收盤價")
plt.plot(avg, 'y-',label="30日線")
plt.grid()

plt.show()


