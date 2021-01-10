# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_08
"""

def factor(n):
    if n == 1: return 1
    return n*factor(n-1)

while True:
    N = int(input("請輸入正整數N="))
    print(f"{N}!={factor(N)}")


