import pickle
class PicklingClass:
    def __init__(self,value1,value2,value3):
        self.value1=value1
        self.value2 = value2
        self.value3 = value3
    def add(self,value):
        self.value1 += value
        self.value2 += value
        self.value3 += value
    #反序列化是调用
    def __getstate__(self):
        print("反序列化是调用 __getstate__")
        return self.value1,self.value2,self.value3
    #序列化是调用
    def __setstate__(self, state):
        self.value1,self.value2,self.value3=state
        print("序列化是调用 __setstate__",state)

p=PicklingClass(100,200,300)
p.add(22)
#打开二进制可写状态的  文件
f= open("pickingTest.pkl","wb")
pickle.dump(p,f)#将序列化的数据 存入二进制可写状态的  文件中
f.close()

#
f=open("pickingTest.pkl","rb")
data=pickle.load(f)
f.close()
print(data.value1,data.value2,data.value3)




