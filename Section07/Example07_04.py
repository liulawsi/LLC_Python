# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_04
"""
def drawStarN(n):
    for i in range(n):
        print("＊",sep="",end="")
    print()
#end def drawStarN--------------------
def drawSpaceN(n):
    for i in range(n):
        print("　",sep="",end="")
#end def drawStarN--------------------

while True:
    N = int(input("請輸入整數N="))
    for i in range(N):
        drawSpaceN(N-i-1)
        drawStarN(i+1)
        
        
        