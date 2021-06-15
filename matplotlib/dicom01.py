# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:43:41 2021

@author: User
"""

import pydicom
import matplotlib.pyplot as plt


aSlice = pydicom.read_file("D:\\1.backup\Desktop\\I0000076")
pixel_data = aSlice.pixel_array
pixel_data = pixel_data * aSlice.RescaleSlope + aSlice.RescaleIntercept
meat = (pixel_data > -200) & (pixel_data < 150)
bone = (pixel_data > 400) 

#huImage = get_pixels_hu(aSlice)


figure = plt.figure()
CT = figure.add_subplot(1,3,1)
Marked = figure.add_subplot(1,3,2)
Marked2 = figure.add_subplot(1,3,3)

# Show some slice in the middle
CT.imshow(pixel_data, cmap=plt.cm.gray)
Marked.imshow(meat, cmap=plt.cm.gray)
Marked2.imshow(bone, cmap=plt.cm.gray)
plt.show()
