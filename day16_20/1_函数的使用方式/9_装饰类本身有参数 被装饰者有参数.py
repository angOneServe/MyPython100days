from functools import wraps
import time

class ClassTime:
    def __init__(self,p1=0,p2=0):               #传递装饰类参数的位置
        self.p1=p1
        self.p2=p2
    def __call__(self,func, *args, **kwargs):   #传递被装饰者 及被装饰者参数
        @wraps(func)
        def warpper(*args,**kwargs):
            start=time.time()
            re=func(*args,**kwargs)
            print(f"运行时间{time.time()-start}，结果为{re},装饰类参数为 {self.p1},{self.p2}")
            return re
        return warpper
#不传参数 需要加()
@ClassTime()
def Func1(fp1=0,fp2=0):
    sum=0
    for i in range(10000):
        for j in range(100):
            sum+=j
    sum=0
    return sum+fp1+fp2

print(Func1())
print(Func1(1))
print(Func1(1,2))

#传参数1个
@ClassTime(1)
def Func1(fp1=0,fp2=0):
    sum=0
    for i in range(10000):
        for j in range(100):
            sum+=j
    sum=0
    return sum+fp1+fp2

print(Func1())
print(Func1(1))
print(Func1(1,2))

#传参数2个
@ClassTime(1,2)
def Func1(fp1=0,fp2=0):
    sum=0
    for i in range(10000):
        for j in range(100):
            sum+=j
    sum=0
    return sum+fp1+fp2

print(Func1())
print(Func1(1))
print(Func1(1,2))
