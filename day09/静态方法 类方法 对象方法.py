class Person:
    is_class=True
    #静态方法
    def __init__(self,name):
        self.name=name
    @staticmethod
    def StaticPrintName(name):
        print(name)
    @classmethod
    def ClassPrintIsClass(cls):
        print("是否为类属性",cls.is_class)
    def instancePrintName(self):
        print(self.name)

#静态方法
Person.StaticPrintName("static")
# 类方法
Person.ClassPrintIsClass()
#实例方法
#Person.instancePrintName() 没有实例，无法运行
Person("instance").instancePrintName()



import time,os
class Clock:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    def run(self):
        self.second+=1
        if self.second%60==0:
            self.second=0
            self.minute+=1
            if self.minute%60==0:
                self.minute=0
                self.hour+=1
                if self.hour%60==0:
                    self.hour=0
    def show(self):
        print("%02d:%02d:%02d"%(self.hour,self.minute,self.second))

    @classmethod    #类方法的应用，创建一个自身类的实例返回
    def Now(cls):
        t=time.localtime()
        clockins=cls(t.tm_hour,t.tm_min,t.tm_sec)
        return clockins

c=Clock.Now()
while True:
    os.system("cls")
    c.run()
    c.show()
    time.sleep(1)