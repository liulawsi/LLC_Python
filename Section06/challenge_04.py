# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    challenge_04
"""

nums=[-2,1,-3,4,-1,2,1,-5,5]

#暴力解
maxSub = nums[0]

for i in range(len(nums)):
    currentSub = nums[i]
    maxSub = max(maxSub, currentSub)
    for k in range(i+1, len(nums)):
        currentSub = currentSub + nums[k]
        maxSub = max(maxSub, currentSub)
        
print(f"maxSub={maxSub}")

#sliding window解
maxSub = nums[0]
currentSub = 0
for i in range(len(nums)):
    currentSub = currentSub + nums[i]
    maxSub = max(maxSub, currentSub)
    if currentSub < 0 : currentSub = 0
    
print(f"maxSub={maxSub}")