# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    Example06_03
"""

nums=[]

for i in range(1,6):
    nums.append(int(input(f"請輸入數字{i}=")))

myMax= max(nums)
myMin = min(nums)
print("=================")
print("最大值=", myMax)
print("最小值=", myMin)

