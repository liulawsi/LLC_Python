# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    challenge_01
"""

while True:
    nums=[0]
    N = int(input("請輸入N="))
    r = 10
    for i in range(N):
        q = r // 19
        nums.append(q)
        r = (r - 19 * q) * 10
    
    print(nums[0],".",sep="",end="")
    for n in nums[1:]:
        print(n,sep="",end="")


