'''
当使用import导入模块时，如果其中除了函数定义外还有其他的可执行代码，
那么这些代码在导入模块时会被执行到，所以我们这些不要执行到的代码，
最好放在if __name__="__main__":条件下，
这样只有当python解释器调用这个脚本是才会执行到
'''
def function1():
    print("测试函数")


print("没有放在条件内的可执行代码")
print("__name__==",__name__)
if __name__=="__main__":
    #只有直接执行本python文件，才可以执行到这个条件下的代码
    print("放在条件内的可执行代码")
if __name__=="day06.importTest":
    print("importTest 模块被导入")
