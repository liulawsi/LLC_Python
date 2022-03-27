# -*- coding: utf-8 -*-
"""
    單元：02_程式語言基本法
    Python 簡易程式範例
    Example02_02
"""

score1 = eval(input("請輸入第一科成績="))
score2 = eval(input("請輸入第二科成績="))
score3 = eval(input("請輸入第三科成績="))

total = score1 + score2 + score3
#Python有一個sum()指令，
#是專門用來對List, Set等作加總的
avg = total / 3

print("\t總成績=", total, "\n\t平均=", avg)

