# -*- coding: utf-8 -*-
"""
    單元：03_流程控制(分支)
    Python 簡易程式範例
    Example03_05
"""

while True:
    season = eval(input("請輸入月份="))

    if season <= 3:
        print(season, "月是春季")
    elif season <= 6:
        print(season, "月是夏季")
    elif season <= 9:
        print(season, "月是秋季")
    elif season <= 12:
        print(season, "月是冬季")