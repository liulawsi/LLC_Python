# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    special_02
"""
print("lambda函式範例")
def square(x):
    return x**2
print(square(5))
#下面的程式等同上面的
square = lambda x : x**2
print(square(5))

print("=======================================")
print("lambda函式當回傳值範例")

def quadratic(a,b,c):
    return lambda x:a*x**2 + b*x + c

func1 = quadratic(1, 3, 2)
func2 = quadratic(2, 1, -6)
print(func1(2))
print(func2(2))

print("=======================================")
print("filter()範例")

def even(x):
    return x if x % 2 == 0 else None

myList = [12,3,45,6,78,9,10]
filter_obj = filter(even,myList)
print("偶數有:",[item for item in filter_obj])

print("=======================================")
print("filter()+lambda範例")

myList = [12,3,45,6,78,9,10]
evenList = list(filter(lambda x: x % 2 == 0,myList))
print("偶數有:",evenList)

print("=======================================")
print("map()+lambda範例")

myList = [1,2,3,4,5,6,7]
doubleList = list(map(lambda x : x*2, myList))
print("myList兩倍：",doubleList)

print("=======================================")
print("reduce()+lambda範例")

from functools import reduce
myList = [1,2,3,4,5,6,7]
mySum = reduce(lambda x,y: x+y, myList)
print("myList總和=",mySum)

print("=======================================")
print("map()+reduce()+lambda範例")

from functools import reduce
def strToInt(s):
    def charToDigit(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
                '6':6, '7':7, '8':8, '9':9}[s]
    return reduce(lambda x,y: x*10+y, map(charToDigit,s))

numStr = '16888'
num = strToInt(numStr)
print("轉換結果是=",num)

