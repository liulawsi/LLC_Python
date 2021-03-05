# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:41:17 2021

@author: Fann

小遊戲：數字記憶遊戲

需要用真正的Win Console才能清除畫面
"""
import random
import os


level = 3
base = 100
 
while True:
    num=random.randint(0, 9*base-1)+base
    print("請記憶：",num)
    
    temp=input("按下Enter開始\n")
    
    os.system("cls")
    
    guess = eval(input("請輸入答案："))
    
    if guess == num:
        print("正確！\n\n")
        level = level+1
        base = base * 10
    else:
        print("錯誤！\n\n")
        level = level-1
        base = base // 10
        if level < 3:
            level = 3
            base = 100

