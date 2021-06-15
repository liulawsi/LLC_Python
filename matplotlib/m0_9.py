# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:35:33 2021

@author: User
"""

import matplotlib.pyplot as plt
import matplotlib
myFont = matplotlib.font_manager.FontProperties(
            fname='C:\Windows\Fonts\mingliu.ttc')

sorts = ["教育", "飲食", "旅遊", "交通"]
money = [10000,15000,8000,8000]
exp=[0, 0, 0, 0.1]

pictures,category_text,percent_text = plt.pie(
    money, labels=sorts, explode=exp,autopct="%2.1f%%", shadow = 'true')

for t in category_text:    #把每一個sorts改成中文字體
    t.set_fontproperties(myFont)
    
plt.legend(loc = "upper left", bbox_to_anchor=(1,1), prop=myFont)

plt.show()


