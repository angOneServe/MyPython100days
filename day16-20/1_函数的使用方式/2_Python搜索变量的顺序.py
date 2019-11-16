#先是看局部作用域
#然后看外层作用域
#再看全局作用域
#最后看内置作用域

#闭包内饰域嵌套定义函数，内部函数可以访问外层的值

def WaiFunc():
    a=1
    a=lambda a:a*2
    return a

print(WaiFunc())

