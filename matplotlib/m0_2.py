# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:17:49 2021

@author: User
"""

import matplotlib.pyplot as plt

x = [2,0,2,1]
y = [7,11,11,6]
x2 = [x for x in range(8)]
y2 = [y**2 for y in range(8)]

figure = plt.figure()
axes1 = figure.add_subplot(1,2,1)
axes2 = figure.add_subplot(1,2,2)

axes1.plot(x, y, 'r--')
axes2.plot(x2, y2, 'bo')

figure.show()