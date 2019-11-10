from multiprocessing import Process
import time

#进程执行多个任务更加省时间
def Task(id,s):
    start=time.time()
    time.sleep(s)
    print(f"进程{id}执行的时间为{time.time()-start}")

def main():
    print("单进程".center(20,"*"))
    start=time.time()
    Task(1,2)
    Task(2,3)
    print(f"总计时间为{time.time()-start}")

    print("多进程".center(20,"*"))
    start=time.time()
    p1=Process(target=Task,args=(1,2))#进程执行的函数名及参数以元组的方式传递给Process
    p1.start()
    p2=Process(target=Task,args=(2,3))
    p2.start()

    beforeT=time.time()
    p1.join(timeout=0.1)#timeout=1   #父进程等待子进程执行完毕，timeout设置超时限制,超过则不再等待子进程，父进程继续向下执行
    afterT=time.time()
    if afterT-beforeT>1:
        print("超时，p1进程执行时间超过0.1")
    else:
        print(afterT-beforeT)

    p2.join(timeout=10) #设置超时限制10秒
    print(f"总计时间为{time.time()-start}")
if __name__=="__main__":
    main()

    #主进程执行完后不会关闭，会等待子进程执行完毕在关闭
