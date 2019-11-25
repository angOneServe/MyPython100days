#值传递与引用传递
#值传递：实参为不可变对象，传递给形参后，形参的值改变，实参的值不变
#引用传递：实参为可变对象，传递给形参后，形参的值改变，实参的值也改变



#普通参数，无默认值
def Func1(a,b,c):
    return a,b,c

#普通参数，有默认值
def Func2(a=1,b=3):
    return a, b
#值传递
def Func3():
    a=1
    def wrapper(b):
        b=2
    wrapper(a)
    print(a)
#引用传递
def Func4():
    a=[1,]
    def wrapper(b):
        b.append(2)
    wrapper(a)
    print(a)

#可变参数 之 *args：表示接受多个参数放到一个元表
def Func5(*arg):
    print(arg)

#可变参数 之 **kwargs：表示接受多个键值对放到一个字典
def Func6(**kwargs):
    print(kwargs)
print(Func1(b=1,a=2,c=2))
print(Func2(b=1,a=2))
Func3()
Func4()
Func5(1,2,3,"ee")
Func6(key1=1,key2="22d")
#