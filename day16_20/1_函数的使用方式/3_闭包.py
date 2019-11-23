#嵌套定义函数，返回内存函数后，外层函数被回收，这个内存函数保存则外层函数里的变量

#如果这个变量是可变类型,地址一直不变
def func1():
    d={"key":1}
    print("outer d地址为)",id(d))
    def func2():
        d["key"]+=1
        print("iner d地址为)",id(d))
        print(d["key"])
    return func2

var=func1()
var()
var()
var()
var()
print("\n\n\n")

#如果这个变量是不可变类型,改变变量值地址会变【这是不可变类型变量的特性】，且在内部使用需要nonlocal
def func1():
    temp=1
    print("outer id(temp)",id(temp))
    def func2():
        nonlocal temp
        temp+=1
        print("iner id(temp)",id(temp))
        print(temp)
    return func2

var=func1()
var()
var()
var()
var()

del(var)#删除后，其数据都不再存在了
