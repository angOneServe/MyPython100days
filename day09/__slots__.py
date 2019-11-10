#__slots__可以进行

print("__slots__中没有name2，实例中不可以动态创建name2")
class SlotsClass:
    __slots__ = {"name","age"}
    def __init__(self):
        self.name="name"
        self.age=1

s=SlotsClass()
print(s.name)
print(s.age)
#s.name2="haha" #报错


print("__slots__中有name2，实例中可以动态创建name2")
class SlotsClass:
    __slots__ = {"name","age","name2"}
    def __init__(self):
        self.name="name"
        self.age=1

s=SlotsClass()
print(s.name)
print(s.age)
s.name2="haha"
print(s.name2)

#影响类的实例属性，但不影响类的属性
print("影响类的实例属性，但不影响类的属性")
SlotsClass.name3="3"
print(SlotsClass.name3)