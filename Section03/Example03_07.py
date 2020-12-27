# -*- coding: utf-8 -*-
"""
    單元：03_流程控制(分支)
    Python 簡易程式範例
    Example03_07
"""

while True:
    print("1.全票, 2.優待票, 3.星光票", end="")
    choice = eval(input("請輸入(1/2/3)："))

    if choice == 1: print("全票一張300")
    elif choice == 2: print("優待票一張250元")
    elif choice == 3: print("星光票一張200")
    print("================================")
# end of while True

