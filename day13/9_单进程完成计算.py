import time
print(f"开始计算。。。")
Nums=[x for x in range(1,70000001)]
before=time.time()
result=0
for x in Nums:
    result+=x
print(f"结果是{result},时间耗费{time.time()-before}")