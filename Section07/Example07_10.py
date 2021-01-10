# -*- coding: utf-8 -*-
"""
    單元：07_函式與方法
    Python 簡易程式範例
    Example07_10
"""
maze=[list("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"),  #30x15
      list("■                            ■"),
      list("■ ■■■■■■■■■■■■■■ ■■■■■■■■■■■ ■"),
      list("■ ■■■■■■    ■■■■ ■■■■■■■■■■■■■"),
      list("■        ■■ ■■    ■■         ■"),
      list("■ ■■■■ ■■■■ ■■■■■■■■ ■■■■■■■ ■"),
      list("■■■■■■ ■■■■■■ ■■■■■■■■■■■■■■ ■"),
      list("■■            ■              ■"),
      list("■■ ■■■■■■■ ■■ ■ ■■■■■■■ ■■■■■■"),
      list("■■ ■■      ■■■■ ■   ■■■ ■■■■■■"),
      list("■■ ■■ ■■ ■■■■■■   ■■■■■   ■■■■"),
      list("■■ ■■ ■■■■ ■■■■ ■■■  ■■■■ ■■■■"),
      list("■■ ■■           ■■■■         ■"),
      list("■■■■■ ■■■■■ ■■■■■■■■■ ■■■■■■E■"),
      list("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")]

def show_maze(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            print(m[y][x],sep="",end="")
        print()        

def Go(y,x):
    found = False
    if maze[y][x] == "E": return True
    else:
        maze[y][x]="."
        if maze[y+1][x] == " " or maze[y+1][x] == "E":
            if Go(y+1, x): found = True
        if maze[y][x+1] == " " or maze[y][x+1] == "E":
            if Go(y, x+1): found = True
        if maze[y-1][x] == " " or maze[y-1][x] == "E":
            if Go(y-1, x): found = True
        if maze[y][x-1] == " " or maze[y][x-1] == "E":
            if Go(y, x-1): found = True

        if found:maze[y][x] = "$"
        
        return found
# def Go end

show_maze(maze)
if Go(1,1):
    print("找到了！")
    show_maze(maze)
else:
    print("沒有找到！")
