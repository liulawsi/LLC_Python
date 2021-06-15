# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:29:39 2021

@author: User
"""

import matplotlib.pyplot as plt

datas = [1,2,1,3,3,2,1,3,2,1,2,4,2,5,2,4,2,5,5,4,4,5,4]
bins = [1,2,3,4,5,6]

plt.axis([0.5,6,0,10])
h = plt.hist(datas, bins,rwidth=0.7,align='left')
print("h[0]=",h[0])
print("h[1]=",h[1])

plt.show()


