# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_05
"""
def drawStarN(n,newLine):
    for i in range(n):
        print("＊",sep="",end="")
    if newLine:print()
#end def drawStarN--------------------
def drawSpaceN(n,newLine):
    for i in range(n):
        print("　",sep="",end="")
    if newLine:print()
#end def drawSpaceN--------------------

while True:
    N = int(input("請輸入整數N="))
    for i in range(N):
        drawStarN(i+1, False)
        drawSpaceN((N-i-1)*2,False)
        drawStarN(i+1, True)
        
        
        