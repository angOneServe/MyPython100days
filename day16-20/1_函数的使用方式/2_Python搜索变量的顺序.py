#先是看局部作用域
#然后看外层作用域
#再看全局作用域
#最后看内置作用域

#嵌套定义函数，返回内存函数后，外层函数被回收，这个内存函数保存则外层函数里的变量

def func1():
    temp=[1,2,3]
    print("outer print(id(temp))",id(temp))
    def func2():
        temp[0]+=1
        print("iner print(id(temp))",id(temp))
        print(temp[0])
    return func2

var=func1()
var()
var()
var()
var()
print("\n\n\n")
def func1():
    temp=1
    print("outer print(id(temp))",id(temp))
    def func2():
        nonlocal temp
        temp+=1
        print("iner print(id(temp))",id(temp))
        print(temp)
    return func2

var=func1()
var()
var()
var()
var()
