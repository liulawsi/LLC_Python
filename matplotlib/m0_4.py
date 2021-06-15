# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:37:58 2021

@author: User
"""

import matplotlib.pyplot as plt

count1 = [100, 204, 288, 199, 189, 166, 190, 170]
date1 = [1, 2, 3, 4, 5, 6, 7, 8]

plt.plot(date1, count1, 'r-')

plt.title("Tourist 2020")
plt.ylabel("Tourist") # y label
plt.xlabel("Month") # x label
plt.show()







#plt.plot(x, y, lw=3, ls='--', label="註解",color='r')

#plt.title("遊客數統計",fontproperties=myfont)
#plt.ylabel("遊客數",fontproperties=myfont) # y label
#plt.xlabel("日期",fontproperties=myfont) # x label