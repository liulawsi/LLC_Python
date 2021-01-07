# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_16
"""

num = 1
while num > 0:
    num = int(input("請輸入正整數N="))
    print(num,"的質因數有：",end="")
    for i in range(2,num):
        while num % i == 0:
            print(i,",",end="")
            num = num // i
        # while-end
    # for-end
# while-end


