# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:29:39 2021

@author: User
"""

import matplotlib.pyplot as plt

count = [100, 204, 288, 199, 189, 166, 190, 170]
date = [1, 2, 3, 4, 5, 6, 7, 8]

plt.plot(date, count, 'r-')
plt.bar(date,count, width = 0.2)

plt.show()


