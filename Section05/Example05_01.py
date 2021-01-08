# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:58:22 2021

@author: User
"""

ii=123
ff=456.789
ss="今天天氣好!"

print("ii1=%7d"%(ii))
print("ii2=%-7d"%(ii))
print("ff1=%10f"%(ff))
print("ff2=%10.2f"%(ff))
print("ff3=%-10.1f"%(ff))
print("ff4=%+10f"%(ff))
print("ss1=%8s"%(ss))
print("ss2=%-8s"%(ss))

print("ii1={:7d}".format(ii))
print("ii2={:<7d}".format(ii))
print("ff1={:10f}".format(ff))
print("ff2={:10.2f}".format(ff))
print("ff3={:<10.1f}".format(ff))
print("ff4={:+10f}".format(ff))
print("ss1={:8s}".format(ss))
print("ss2={:^8s}".format(ss))



print("{name}的身高是{h:4d}公分,體重是{w:5.1f}公斤".format(w=68,name="劉老師",h=168))

name="劉老師"
height=168
weight=68

print(f"{name}的身高是{height:4d}公分,體重是{weight:5.1f}公斤")

