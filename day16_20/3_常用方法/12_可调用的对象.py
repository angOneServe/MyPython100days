#对象成为一个方法

class CallClass:
    def __call__(self, *args, **kwargs):
        print("CallClass")
        for v in args:
            print(v,end=" ")
        print()
        for k,v in kwargs.items():
            print(k,v,end=" ")

c= CallClass()
c("1","1",a=2)