# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    challenge_03
"""

map=[[1,1,3,5,2],
     [2,2,1,1,4],
     [1,5,2,2,1],
     [1,1,2,2,3]]
cost=[]

line=[map[0][0]]
for k in range(1,len(map[0])):
    line.append(map[0][k]+line[k-1])
cost.append(line)
   
for i in range(1,len(map)):
    line=[map[i][0]+cost[i-1][0]]
    for k in range(1,len(map[i])):
        up = map[i][k]+cost[i-1][k]
        left = map[i][k]+line[k-1]
        line.append(min(up,left))
    cost.append(line)
    
#輸出結果
for l in map: 
    for i in l:       
        print(f"{i:^5}",sep="",end="")
    print()
print()
    
for l in cost: 
    for i in l:       
        print(f"{i:^5}",sep="",end="")
    print()