# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:06:11 2021

@author: User
"""
import random

while True:
    ans=random.sample('1234567890',4)
    print ("======  猜數字  ======")
    print (ans)
    while True:
        guessStr = input("輸入4個不同數字:")
        guess = list(guessStr)
        nA = 0; 
        nB = 0;
        for i in range(4):
            for k in range(4):
                if ans[i] is guess[k]:
                    if i == k:
                        nA = nA + 1
                    else:
                        nB = nB + 1        
        if nA == 4:
            break
        else:
            print(nA,"A", nB, "B")
            
    print("        猜中了！！！")



