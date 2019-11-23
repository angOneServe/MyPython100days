"""
抽象方法：
抽象方法表示基类的一个方法，没有实现，所以基类不能实例化，子类实现了该抽象方法才能被实例化。
Python的abc提供了@abstractmethod装饰器实现抽象方法，下面以Python3的abc模块举例。

@abstractmethod：
见下图的代码，基类Foo的fun方法被@abstractmethod装饰了，所以Foo不能被实例化；子类SubA没有实现基类的fun方法也不能被实例化；子类SubB实现了基类的抽象方法fun所以能实例化。


在Python3.4中，声明抽象基类最简单的方式是子类话abc.ABC；Python3.0到Python3.3，必须在class语句中使用metaclass=ABCMeta；Python2中使用__metaclass__=ABCMeta
"""
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def say(self):
        pass
class bilibiler(Person):
    def say(self):
        print("bilibili...")

class douyiner(Person):
    def say(self):
        print("douyin...")
class noner(Person):
    pass

if __name__=="__main__":
    #p=Person()  #TypeError: Can't instantiate abstract class Person with abstract methods say
    b=bilibiler()
    b.say()

    d=douyiner()
    d.say()

    #n=noner()   #TypeError: Can't instantiate abstract class noner with abstract methods say

