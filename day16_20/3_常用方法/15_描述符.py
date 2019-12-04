#利用__get__与__set__实现了单位的相互转换

class M:
    def __init__(self,value=0):
        self.value=value
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value=float(value)
    def __str__(self):
        return f"{self.value}m"
class CM:
    def __init__(self):
        self.value=-1
    def __get__(self, instance, owner):
        self.value=instance.m*100
        return instance.m*100
    def __set__(self, instance, value):
        self.value=value/100.0
        instance.m=value/100.0
    def __str__(self):
        return f"{self.value}cm"

class Distance:
    m=M()
    cm=CM()

    print("Distance",m,cm)

    def __init__(self,value):
        self.m=value


d=Distance(100)
print(d.cm) #为什么这里不带单位，不会调用CM的__str__???貌似是因为调用了__get__
print(d.m)  #为什么这里不带单位，不会调用M的__str__???

d.cm=1
print(d.cm)
print(d.m)

d.m=1
print(d.cm)
print(d.m)
#调用M的__str__
print(M(1))
