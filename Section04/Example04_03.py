# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_03
"""

while True:
    num = int(input("請輸入整數N="))    
    for i in range(1,num+1):
        print(i,end="")
        if i != num:
            print("+",end="")
    # for-end
#while end



