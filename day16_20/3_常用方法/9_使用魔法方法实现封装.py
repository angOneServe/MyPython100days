class Person:
    def __init__(self):
        self.name="name"

    
    #访问不存在的属性时才会调用
    def __getattr__(self, item):
        self.__setattr__(item,-1)
        #return self.item  #取 key为"item" 的值
        return self.__dict__[item]
        print (f"__getattr__")
        # 访问不存在和存在的属性时，都会被调用

    '''
    #无论属性是否存在，访问就会调用此方法
    def __getattribute__(self, item):
        pass

    '''

    #赋值操作，无论属性是否存在
    def __setattr__(self, key, value):
        #self.key=value
        #每次赋值都会调用__setattr_，所有这里会导致递归（普通递归次数限制为1000，可改）,直到程序奔溃
        #self.key=value等同于self.__setattr__(key,value)
        self.__dict__[key]=value
        print(f"你正在给{key}赋值{value}")
p=Person()._name2
print(p)