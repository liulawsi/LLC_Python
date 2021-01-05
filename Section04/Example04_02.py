# -*- coding: utf-8 -*-
"""
    單元：04_串列(List)一定要認識
    Python 簡易程式範例
    Example04_02
"""

nums=[]

nums.append(int(input("請輸入數字1=")))
nums.append(int(input("請輸入數字2=")))
nums.append(int(input("請輸入數字3=")))
nums.append(int(input("請輸入數字4=")))
nums.append(int(input("請輸入數字5=")))

mySum= sum(nums)
avg = mySum / 5
print("=================")
print("總和=", mySum)
print("平均=", avg)

