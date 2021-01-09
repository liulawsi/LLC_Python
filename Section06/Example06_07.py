# -*- coding: utf-8 -*-
"""
    單元：06_串列(List)一定要認識
    Python 簡易程式範例
    Example06_07
"""
scores=[["數學", "英文","理化"],
        ["Jack",85,78,65],
        ["Rose",75,85,69],
        ["Peter",63,67,95],
        ["Paul",94,92,88],
        ["Sam",74,65,73] ]

print("%8s"%(""),end="")
for title in scores[0]:
    print(f"{title:^6s}",end="")
    
print()

for index in range(1,6):
    print(f"{scores[index][0]:^8s}",end="")
    for s in scores[index][1:]:
        print(f"{s:^8d}", end="")
    print()
print("============================================")
print("%8s"%(""),end="")
for n in range(1,6):
    name = scores[n][0]
    print(f"{name:^8s}",end="")
    
print()

for index in range(3):
    print(f"{scores[0][index]:^6s}",end="")
    for s in range(1,6):
        print(f"{scores[s][index+1]:^8d}", end="")
    print()
    
    
my2DList=[[0],
          [1,2],
          [3,4,5],
          [6,7,8,9]
          ["string", 3.3,['a','b']]]




