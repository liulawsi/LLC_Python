# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_06
"""
def BMI(height,weight):
    return weight/(height*height)
#end def BMI---------------------------

while True:
    h = eval(input("請輸入身高(公尺)="))
    w = eval(input("請輸入體重(公斤)="))
    bmi = BMI(h,w)
    print(f"你的BMI={bmi:4.1f}")
        
        
        