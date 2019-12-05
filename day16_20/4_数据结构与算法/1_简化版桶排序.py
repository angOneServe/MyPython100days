'''
桶排序就是：

对分数（0-100）排序，需要101个桶
'''

#初始化排序数组
inputs=[]
while True:
    cmd=input("请输入分数（0--100）q退出：")
    if cmd=="q":
        break

    if not cmd.isdigit():
        continue
    inputs.append(cmd)
#排序
tongs=[0 for x in range(101)]
for v in inputs:
    tongs[int(v)]+=1

#输出已排序的队列
for i in range(100):
    for j in range(tongs[int(i)]):
        print(i)





