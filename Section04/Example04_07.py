# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_07
"""

while True:
    result=1
    num =int(input("請輸入整數N="))
    for i in range(1,num):
        if num % i == 0:
            print(i,",",end="")
    # for-end
#while end


    