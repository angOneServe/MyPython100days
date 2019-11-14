import time
from multiprocessing import Process,Queue
def CaculateSum_(nums,start,end,re_q):
    sum=0
    for index in range(start,end):
        sum+=nums[index]
    re_q.put(sum)
    #print(sum)
def CaculateSum(nums,start,end,re_q):
    Process(target=CaculateSum_,args=(nums,start,end,re_q)).start()

print(f"开始计算。。。")
Nums=[x for x in range(1,70000001)]
before=time.time()
result=0
re_queue=Queue()
for x in range(7):
    CaculateSum_(Nums,x*10000000,(x+1)*10000000,re_queue)

result=0
while not re_queue.empty():
    result+=re_queue.get()


print(f"结果是{result},时间耗费{time.time()-before}")