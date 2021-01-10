# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_09
"""

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1)+fib(n-2)

for i in range(20):
    print(f"{fib(i)},",sep="",end="")


