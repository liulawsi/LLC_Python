# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:17:49 2021

@author: User
"""
import twstock
import matplotlib.pyplot as plt

x = [2,0,2,1]
y = [7,11,11,6]
x2 = [x for x in range(8)]
y2 = [y**2 for y in range(8)]

figure = plt.figure()
axes1 = figure.add_subplot(1,2,1) #在1x2的布置中的第1個axes
axes2 = figure.add_subplot(1,2,2) #在1x2的布置中的第2個axes

axes1.plot(x, y, 'r--')
axes2.plot(x2, y2, 'bo')

figure.show()