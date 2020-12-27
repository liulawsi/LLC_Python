# -*- coding: utf-8 -*-
"""
    單元：03_流程控制(分支)
    Python 簡易程式範例
    Example03_08
"""

while True:
    print("1.全票, 2.優待票, 3.星光票", end="")
    choice = eval(input("請輸入(1/2/3)："))
    num = eval(input("請輸入買幾張："))
    
    if choice == 1:
        total = num * 300;
    elif choice == 2:
        total = num * 250;
    elif choice == 3:
        total = num * 200;
    print("票價總額為", total, "元")
    print("================================")
# end of while True
