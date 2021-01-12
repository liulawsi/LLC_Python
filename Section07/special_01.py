# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    special_01
"""
print("call by sharing範例")
class Count:
    def __init__(self, count=0):
        self.count = count

def increment(c, times):
    c.count += 1
    print('c:', c.count)
    times += 1
    print('t:', times)

def main():
    c = Count()
    times = 0
    for i in range(100):
        increment(c, times)

main()

print("=========================================")
print("任意數量參數範例")
def favorite(*places):
    print("喜歡去的地方：",end="")
    for p in places:
        print(f"{p},",sep="",end="")
    print()
    
favorite("台南")    
favorite("台北","墾丁","花蓮")
    
print("=========================================")
print("函數當參數範例")
def add(a,b):
    return a+b
def sub(x,y):
    return x-y
def myFunc(func,v1,v2):
    return func(v1,v2)

result = myFunc(add,5,3)
print(result)
result = myFunc(sub,5,3)
print(result)

print("=========================================")
print("內嵌函式範例")
def outer(a):
    b=5
    def inner(x):
        return x*2+b
    return inner(a)
result = outer(2)
print(result)

print("=========================================")
print("把內嵌函式當回傳值範例")
def outer():
    b=5
    def inner(x):
        return x*2+b
    return inner
f = outer()
result = f(2)
print(result)

print("=========================================")
print("二次函數 ax2+bx+c的計算")
def quadratic(a,b,c):
    def inner(x):
        return a*x*x + b*x + c
    return inner

f1 = quadratic(1,2,3)
f2 = quadratic(2,1,4)

result = f1(2)
print(result)
result = f2(2)
print(result)

