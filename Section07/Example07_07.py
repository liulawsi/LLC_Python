# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_07
"""
def myPow(x,n):
    result = 1
    for i in range(n):
        result = result * x
    return result
#end def myPow---------------------------
    
while True:
    x = eval(input("請輸入x="))
    n = eval(input("請輸入n="))
    result = myPow(x,n)
    print(f"{x}的{n}次方={result:<10f}")
        
        

    
    