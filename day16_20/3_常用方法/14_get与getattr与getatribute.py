class A:
    a=1
    def __getattr__(self, item):
        print("__getattr__被调用")
    #有__getattribute__不会再调用__getattr__
    def __getattribute__(self, item):
        print("__getattribute__被调用")

    def __get__(self, instance, owner):
        print("__get__被调用",instance,owner)
class B:
    a=A()
    def __init__(self):
        self.aa=A()

T1=A()
T2=B()
print(T1.a)  #__getattribute__被调用
print(T1.b)  #__getattribute__被调用
print(T2.a)  #__get__被调用  B的实例去调用 ，作为类成员是会调用__get__，instance为T2.a实例本身，owner为T2
print(B.a)  #__get__被调用 B类去调用，作为实例成员是不会调用__get__  instance为None，owner为T2
print(T2.aa)  #__get__被调用 作为实例成员是不会调用__get__