# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    challenge_02
"""

while True:
    N = int(input("請輸入N="))
    M = int(input("請輸入M="))
    pascal=[[1],[1,1]]
    for i in range(2,N+1):
        line=[1]
        for k in range(1,i):
            line.append(pascal[i-1][k-1]+pascal[i-1][k])
        line.append(1)
        pascal.append(line)
    
    print(f"{N}取{M}的組合數={pascal[N][M]}")

