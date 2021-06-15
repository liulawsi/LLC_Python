# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:50:29 2021

@author: User
"""

import twstock
import matplotlib.pyplot as plt
import matplotlib
myFont = matplotlib.font_manager.FontProperties(
            fname='C:\Windows\Fonts\mingliu.ttc')

stock6547 = twstock.Stock("6547")
print("股票代號：", stock6547.sid)
print("收盤價：",stock6547.price)

plt.title("高端疫苗", fontproperties=myFont, fontsize = 20)
plt.plot(stock6547.price, 'r-')
plt.show()


