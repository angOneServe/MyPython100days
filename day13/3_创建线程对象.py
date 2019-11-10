from threading import Thread
import time
class Task(Thread):
    def __init__(self,name):
        # noinspection PyArgumentList
        super().__init__()
        self.name=name
    def run(self):#重写Thread的run函数
        print(self.name,"开始")
        start=time.time()
        time.sleep(3)
        print(f"线程{self.name}结束,时间为{time.time()-start}")

def main():
    start=time.time()
    t1=Task(1)
    t1.start()

    t2=Task(2)
    t2.start()

    t1.join()
    t2.join()

    print(f"总计用时{time.time()-start}")

if __name__=="__main__":
    main()
