class Test:
    #__new__需要执行父类的__new__方法，得到instance，处理后返回
    def __new__(cls, *args, **kwargs):
        ins=super().__new__(cls,*args,**kwargs)
        print("__new__")
        return ins
    def __init__(self):
        print("__init__")

    def __del__(self):
        print("__del__","对象即将被销毁")

Test()
print("wtith后面")
