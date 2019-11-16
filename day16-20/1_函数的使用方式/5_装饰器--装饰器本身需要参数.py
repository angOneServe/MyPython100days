'''
装饰器无参数
 def Shenghaizi_(被装饰的函数):
        def Shenghaizi_WorkFunc(被装饰的函数的参数):
            if 装饰器参数sex=="man":
                print("不能怀孩子")
            if 装饰器参数sex=="women":
                print("能怀孩子")

            被装饰的函数的参数=被装饰的函数的参数+200
            被装饰的函数(被装饰的函数的参数)
        return Shenghaizi_WorkFunc

'''


def Shenghaizi(装饰器参数sex):                       #如果装饰器无参数，可不要这一层
    def Shenghaizi_main(被装饰的函数):
        def Shenghaizi_WorkFunc(被装饰的函数的参数):
            if 装饰器参数sex=="man":
                print("不能怀孩子")
            if 装饰器参数sex=="women":
                print("能怀孩子")

            被装饰的函数的参数=被装饰的函数的参数+200
            被装饰的函数(被装饰的函数的参数)
        return Shenghaizi_WorkFunc
    return Shenghaizi_main

'''
执行过程

Shenghaizi(装饰器参数sex)
    返回 Shenghaizi_main
    
    Shenghaizi_main(被装饰的函数)
        返回Shenghaizi_WorkFunc
        
        Shenghaizi_WorkFunc()  #依据前面 装饰器参数 被装饰的函数 等参数进行执行
            执行增加的代码
            被装饰的函数()
        
'''
@Shenghaizi("man")
def man(age):
    print("我是man")
    print("我要工作")
    print(f"我今年{age}岁")
@Shenghaizi("women")
def woman(age):
    print("我是woman")
    print("我要工作")
    print(f"我今年{age}岁")
print(man.__name__,man.__doc__)
print(woman.__name__,woman.__doc__)
man(1)
woman(1)
