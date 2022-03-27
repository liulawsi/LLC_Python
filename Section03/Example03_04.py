# -*- coding: utf-8 -*-
"""
    單元：03_流程控制(分支)
    Python 簡易程式範例
    Example03_04
"""
while True:
    a = eval(input("請輸入整數A="))
    b = eval(input("請輸入整數B="))
    c = eval(input("請輸入整數C="))

    if a > b :
        if a > c:
            print("The Max=", a)
        else:
            print("The Max=", c)
    else:
        if b > c:
            print("The Max=", b)    
        else:
            print("The Max=", c)
"""    
#方法二  
if a >= b and a >= c:
    theMax=a 
if b >= a and b >= c:
    theMax=b
if c >= a and c >= b:
    theMax=c
print("The Max=", theMax)
        
#方法三
theMax = max(a,b,c)        
print("max()=", theMax)

"""