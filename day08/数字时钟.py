import time
import os
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
def main():
    c=Clock(11,53,0)
    while True:
        c.run()
        os.system("cls")
        c.show()
        time.sleep(1)
if __name__=="__main__":
    main()


