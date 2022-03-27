# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:37:58 2021

@author: User
"""

import matplotlib.pyplot as plt
import matplotlib
myfont = matplotlib.font_manager.FontProperties(
            fname='C:\Windows\Fonts\mingliu.ttc')

count1 = [100, 204, 288, 199, 189, 166, 190, 170]
date1 = [1, 2, 3, 4, 5, 6, 7, 8]
count2 = [90, 210, 228, 299, 169, 176, 194, 172]
date2 = [1, 2, 3, 4, 5, 6, 7, 8]

plt.plot(date1, count1, 'r-', label="2020年")
plt.plot(date2, count2, 'b--', label="2021年")
plt.legend(prop=myfont)
plt.grid()
plt.title("遊客數 2020 vs 2021",fontproperties=myfont)
plt.ylabel("人數",fontproperties=myfont) # y label
plt.xlabel("月份",fontproperties=myfont) # x label
plt.text(4,299,"最大值",fontproperties=myfont)
plt.savefig("tourist2021.jpg")
plt.show()





#plt.title("遊客數統計",fontproperties=myfont)
#plt.ylabel("遊客數",fontproperties=myfont) # y label
#plt.xlabel("日期",fontproperties=myfont) # x label