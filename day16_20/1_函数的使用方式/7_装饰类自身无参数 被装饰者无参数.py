from functools import wraps
import time

#装饰类本身无参数
class ClassTime:
    def __init__(self,func):
        self.func=func
    def __call__(self,):
        start=time.time()
        re=self.func()
        print(f"运行时间{time.time()-start}，结果为{re}")
        return re
@ClassTime
def Func1():
    sum=0
    for i in range(10000):
        for j in range(100):
            sum+=j
    return sum

print(Func1())
print(Func1())
