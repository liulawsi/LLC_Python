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
    
    '''
    #用enumerate的結果取得(顯示)方案
    print()
    results = enumerate(numbers[2:],2)
    for item in results:
        if item[1] == 0: print(item[0],",",sep="",end="")
    '''
# while end

