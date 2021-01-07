# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_10
"""

while True:
    num =int(input("請輸入整數N="))
    for i in range(num):
        for k in range(num-i):
            print("＊",end="")
        # for-end
        print()
    # for-end
#while end


    