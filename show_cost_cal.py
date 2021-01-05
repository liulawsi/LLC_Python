# -*- coding: utf-8 -*-
"""
  給一整數陣列，印出所有排列
  用遞迴函式
  2021/1/2
  fann
"""

def countCost():
    global maxScore
    global costs
    global scores
    tCost=0
    tScore = 0
    for n in answer:
        nCost = tCost + costs[n-1]
        if nCost <= limitCost :
            tCost = nCost
            tScore = tScore + scores[n-1]
            if tScore >= maxScore :maxScore = tScore
        else:
            break;
    #print("  --->", tScore)
# end countCost 
    
    
def MyPermute(parts):   
    #
    if len(parts) == 0:
        #for val in answer:print(val,",",end="")
        countCost()
        #print()
        return;
        
    for i in range(len(parts)):
        n = parts[0]
        del parts[0]
        answer.append(n)
        MyPermute(parts)
        del answer[len(answer)-1]
        parts.append(n)
# end MyPermute()        
    
nums=[]
answer=[]

costs=[]
scores=[]

limitCost = 0    
maxScore = 0
n = 0

line = input().split()
limitCost = int(line[0])
n = int(line[1])

for i in range(n):
    nums.append(i+1)
    line = input().split()
    scores.append(int(line[0]))
    costs.append(int(line[1]))
    
MyPermute(nums)

print("MAX Score=", maxScore)