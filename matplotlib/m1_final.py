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
stock6547.fetch_from(2020, 8)

prices1 = list(filter(None, stock6547.price))
avg30 = stock6547.moving_average(prices1, 30)
avg5 = stock6547.moving_average(prices1, 5)
prices2 =prices1[len(prices1)-len(avg30):]
avg5 = avg5[len(avg5)-len(avg30):]

stockMax = max(prices2)
maxidx = prices2.index(stockMax)

plt.plot(prices2, 'r-', label="收盤價")
plt.plot(avg30, 'y-',label="30日線")
plt.plot(avg5, 'c-',label="5日線")

plt.text(maxidx-80, stockMax, "最高價："+ str(stockMax), fontproperties=myFont)
plt.legend(prop=myFont)
plt.xlabel("2020年8月以來交易天數", fontproperties=myFont)
plt.ylabel("股價", fontproperties=myFont)
plt.grid()
plt.savefig("D:\\1.backup\Desktop\\高端股價.jpg", dpi=300)
plt.show()


