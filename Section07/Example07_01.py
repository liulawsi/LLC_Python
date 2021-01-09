# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_01
"""

def SayHi(name):
    print(f"Hello, {name} !")
    
while True:
    nameStr = input("請問大名是？")
    SayHi(nameStr)

