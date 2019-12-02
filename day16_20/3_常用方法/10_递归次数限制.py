import sys
sys.setrecursionlimit(1500) #设置最大递归数为1500

def Digui(count,max):
    print(count)
    if count>=max:
        return
    Digui(count+1,max)

Digui(1,1000)