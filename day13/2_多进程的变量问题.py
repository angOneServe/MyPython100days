from multiprocessing import Process
from threading import Thread
import time
counter=10

def AddOne(name):
    global counter
    while counter>0:
        time.sleep(0.01)
        counter-=1
        print(name,counter)

def main():
    print("多进程".center(20,"*"))
    p1=Process(target=AddOne,args=("p1",))
    p1.start()
    p2=Process(target=AddOne,args=("p2",))
    p2.start()
    p1.join()
    p2.join()

    print("单进程".center(20,"*"))
    global counter
    counter=10
    AddOne("p1")
    AddOne("P2")


    counter=10
    print("多线程".center(20,"*"))
    t1=Thread(target=AddOne,args=("t1",))
    t1.start()
    t2=Thread(target=AddOne,args=("t2",))
    t2.start()
    t1.join()
    t2.join()

if __name__=="__main__":
    main()
