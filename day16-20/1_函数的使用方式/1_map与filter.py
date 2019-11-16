#map(函数,数据序列1,数据序列2,...)
"""
参数1为一个函数
参数2 参数3 参数n:为数据序列，看函数需要几个参数，就要几个数据序列，谢丽尔可以是字符串，元组，列表等

返回值：返回一个全新的列表，不影响原有列表
"""
items=list(map(lambda x:x*2,[1,2,3]))
print(items)
items=list(map(lambda x,y:x*2*y,[1,2,3],[4,5,6]))
print(items)

#filter(判断函数，可迭代对象)

items=filter(lambda x:x%2==0,[2,3,4,5,6,33])
for v in items:
    print(v,end=" ")

#global声明全局变量
#nonlocal 声明使用嵌套作用域的变量
print()
temp="Func的外部变量"  #外部变量
def Func():
    temp="Func的内部变量，Funca的外部变量" #对于Func这个是内部变量，对于Funca这个是外部变量
    print(temp)
    def Funca():
        nonlocal temp       #使用的是离这里最近的外部变量【嵌套变量】，即值为“Func的内部变量，Funca的外部变量”的那个
        temp="nonlocal" #内部变量
        print(temp)
    Funca()
    print(temp)
Func()
print(temp)
