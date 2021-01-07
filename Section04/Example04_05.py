# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_05
"""

while True:
    result=1
    num =int(input("請輸入整數N="))
    for i in range(1,num):
        print(i,"x",end="")
        result = result * i
    # for-end
    result = result * num
    print(num,"=",result)
#while end