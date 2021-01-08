# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    Example06_02
"""

nums=[]
#mySum = 0
for i in range(1,6):
    nums.append(int(input(f"請輸入數字{i}=")))
    #mySum = mySum + nums[i-1]

mySum= sum(nums)
avg = mySum / 5
print("=================")
print("總和=", mySum)
print("平均=", avg)

