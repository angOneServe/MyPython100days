class People:
    def say(self):
        print ("say")
    def eat(self):
        print ("eat")
p=People()
#获取属性
#getattr(实例，方法名【字符串】,默认方法【方法】)  返回一个方法
method=getattr(p,"say",p.eat)
method()

#设置属性
method=lambda :print("lambda method")
setattr(p,"method",method)
p.method()

#删除属性
delattr(p,"method")
getattr(p,"method",lambda :print("属性不存在"))()

#属性检测
print(hasattr(p,"eat"))
print(hasattr(p,"eat2"))

