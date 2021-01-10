# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_11
"""

while True:
    num =int(input("請輸入整數N="))
    for i in range(num):
        for p in range(num-i-1):
            print("　",sep="",end="")
        for k in range(i+1):
            print("＊",sep="",end="")
        print()
    # for-end
#while end


    