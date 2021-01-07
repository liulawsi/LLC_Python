# -*- coding: utf-8 -*-
"""
    單元：04_迴圈大法
    Python 簡易程式範例
    Example04_15
"""

import random

while True:
    bomb = random.randint(1,100)
    top = 100
    bottom = 1
    guess = 0
    while guess != bomb:
        print("請輸入正整數(", bottom,"～",top,")=")
        guess = int(input())
        if guess > bomb:
            top = guess - 1
        if guess < bomb:
            bottom = guess + 1
    # while-end
    print("========================")
    print("爆！炸彈是", guess,"。")
    print("========================\n\n")
# while-end


