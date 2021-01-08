# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    Example06_04
"""
N = 0
while N >= 0:
    N = int(input("請輸入整數="))

    numbers=[]
    while N > 0:
        numbers.append(N % 10)
        N = N // 10
    
    print(numbers)


