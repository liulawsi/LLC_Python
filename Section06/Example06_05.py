# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    Example06_05
"""
N = 1
while N > 0:
    N = int(input("請輸入正整數N="))
    numbers = [0 for i in range(N+1)]
    
    for i in range(2,N+1):
        index = i + i
        while index <= N:
            numbers[index] = numbers[index] + 1
            index = index + i
        # while-end
    # for-end
    
    for i in range(2,N+1):
        if numbers[i] == 0: print(i,",",sep="",end="")
# while end

