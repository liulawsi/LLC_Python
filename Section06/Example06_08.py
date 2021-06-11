# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    Example06_08
"""

while True:
    num = int(input("請輸入層數="))
    pascal=[[1],[1,1]]
    for i in range(2,num):
        line=[1]
        for k in range(1,i):
            line.append(pascal[i-1][k-1]+pascal[i-1][k])
        line.append(1)
        pascal.append(line)
    
    for row in pascal:
        print(row)
# while-end

