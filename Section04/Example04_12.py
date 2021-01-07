# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_12
"""

while True:
    num =int(input("請輸入整數N="))
    for i in range(2,num+1):
        isPrime = True
        for k in range(2,i):
            if i % k == 0:
                isPrime = False
        if isPrime:
            print(i,",",end="")
    # for-end
#while end


    