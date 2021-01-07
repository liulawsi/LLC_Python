# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_04
"""

while True:
    total=0
    num = int(input("請輸入整數N="))    
    for i in range(1,num):
        print(i,"+",end="")
        total = total + i
    # for-end
    total = total + num
    print(num,"=",total)
#while end

