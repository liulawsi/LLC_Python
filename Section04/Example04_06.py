# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_06
"""

while True:
    result=1
    a = int(input("請輸入整數a="))
    num =int(input("請輸入整數n="))
    for i in range(num):
        result = result * a
    # for-end
    print(a,"的",num,"次方=",result)
#while end