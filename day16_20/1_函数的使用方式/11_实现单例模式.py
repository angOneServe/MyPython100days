from functools import wraps
def Singler(cl):
    instances={}

    @wraps(cl)
    def wrapper(*a,**b):
        if cl not in instances:
            instances[cl]=cl(*a,**b)
        return instances[cl]
    return wrapper

@Singler
class C1:
    def __init__(self):
        print("init")
        self.num=0
    def run(self):
        self.num+=1
        print(self.num)

class C2:
    def __init__(self):
        print("init")
        self.num=0
    def run(self):
        self.num+=1
        print(self.num)
if __name__=="__main__":
    print("单例")
    a=C1()
    a.run()
    a.run()
    a=C1()
    a.run()
    a.run()
    print("非单例")
    a=C2()
    a.run()
    a.run()
    a=C2()
    a.run()
    a.run()
