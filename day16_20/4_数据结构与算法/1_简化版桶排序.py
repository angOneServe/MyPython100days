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
'''
BIG O标记法
n:数据规模
f(n):代码执行次数与数据规模的关系
t(n):代码执行时间与数据规模的关系
t(n)=O(f(n))
'''
#排序
# f(n)=1+n
# 时间复杂度：t(n)=O(1+n)=O(n)
#空间复杂度：O(n)
tongs=[0 for x in range(101)]
for v in inputs:
    tongs[int(v)]+=1

#输出已排序的队列
for i in range(100):
    for j in range(tongs[int(i)]):
        print(i)





