#@property实际上就是定义了一个属性，如shuxing这个属性外界可以读值，写值
#这个属性可以自定义读写值得一些操作，即使用@shuxing.setter和@shuxing.getter创建同名方法进行设置
class Person:
    def __init__(self):
        self._name=""
        self._age=-1
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name="设置器"

    @property           #定义一个属性
    def age(self):
        return "年龄为："+str(self._age)
    @age.getter
    def age(self):      #定义属性的读值
        return "你的年龄为："+str(self._age)
    @age.setter         #定义属性的写值
    def age(self,age):
        self._age=age+1


    
p=Person()
p.name=""
p.age=4     #age属性写值函数被执行，self._age=age+1
print(p.name)
print(p.age)

p._age=55   #直接给_age写值，并不影响属性age的值
print(p.name)
print(p.age)