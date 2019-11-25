'''
python2.3之前，搜索是深度优先
python2.3开始，使用广度优选算法

'''
import inspect


class A():
    def __init__(self):
        print('enter A')
        print('leave A')
class A2():
    def __init__(self):
        print('enter A')
        print('leave A')

class B(A,A2):#b a
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):#c a
    def __init__(self):
        print('enter C')
        super().__init__()
        print("ff")
        super().__init__()
        print('leave C')


class D(B, C):# d b c
    def __init__(self):
        print('enter D')
        super().__init__()#super()得到B类，只进行D后面B的__init__()方法
        print('leave D')


d = D()
print(inspect.getmro(D))#
print(inspect.getmro(B))#
print(D.mro())#
print(B.__mro__)#
