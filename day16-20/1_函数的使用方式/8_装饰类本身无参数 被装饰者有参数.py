from functools import wraps
import time

class ClassTime:
    def __init__(self,func):                #传递被装饰者
        self.func=func
    def __call__(self, *args, **kwargs):    #传递被装饰者参数
        start=time.time()
        re=self.func(*args,**kwargs)
        print(f"运行时间{time.time()-start}，结果为{re}")
        return re

@ClassTime
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
