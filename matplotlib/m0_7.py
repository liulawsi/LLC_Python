# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:29:39 2021

@author: User
"""

import matplotlib.pyplot as plt

count = [100, 204, 288, 199, 189, 166, 190, 170]
count2 = [90, 210, 228, 299, 169, 176, 194, 172]
date = [1, 2, 3, 4, 5, 6, 7, 8]
x1 = [0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9, 7.9]
x2 = [1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1]

plt.plot(date, count, 'r-')
plt.plot(date, count2, 'b--')
plt.bar(x1,count, width = 0.2)
plt.bar(x2,count2, width = 0.2)

plt.show()


