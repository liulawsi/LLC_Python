# -*- coding: utf-8 -*-
"""
    單元：03_流程控制(分支)
    Python 簡易程式範例
    Example03_06
"""

while True:
    score = eval(input("請輸入成績="))
    
    if score >= 90: print(score,"分是A級")
    elif score >=80: print(score,"分是B級")
    elif score >=70: print(score,"分是C級")
    elif score >=60: print(score,"分是D級")
    else: print(score,"分是E級")
# end of while True

