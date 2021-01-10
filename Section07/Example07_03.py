# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_03
"""

def drawStarN(n):
    for i in range(n):
        print("＊",sep="",end="")
    print()
#end def drawStarN--------------------

while True:
    N = int(input("請輸入整數N="))
    for i in range(1,N+1):
        drawStarN(i)
        
    for i in range(N-1,0,-1):
        drawStarN(i)
        
        