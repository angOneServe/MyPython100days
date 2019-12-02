#利用__get__与__set__实现了单位的相互转换

class M:
    def __init__(self,value=0):
        self.value=value
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value=float(value)
class CM:
    def __get__(self, instance, owner):
        return instance.m*100
    def __set__(self, instance, value):
        instance.m=value/100.0

class Distance:
    m=M()
    cm=CM()
    def __init__(self,value):
        self.m=value


d=Distance(100)
print(d.cm)
print(d.m)

d.cm=1
print(d.cm)
print(d.m)

d.m=1
print(d.cm)
print(d.m)

