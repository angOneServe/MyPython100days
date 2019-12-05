
'''
cmpAttr:默认比较自身，有的话就是比较自身名为cmpAttr的属性
'''
def MaoPaoSort(datas,cmpAttr=""):
    temp=datas[0]
    length=len(datas)
    #从小到大排序

    #如果comAttr不为空
    if cmpAttr!="":
        for i in range(length-1):
            #遍历未排序序列 从第一到倒数第二个 list[0]---list[length-i-1]
            for j in range(0,length-i-1):
                if getattr(datas[j],cmpAttr)>getattr(datas[j+1],cmpAttr):
                    #交换数据
                    temp=datas[j]
                    datas[j]=datas[j+1]
                    datas[j+1]=temp

        return
    print(cmpAttr)
    #遍历length-1遍数据
    for i in range(length-1):
        #遍历未排序序列 从第一到倒数第二个 list[0]---list[length-i-1]
        for j in range(0,length-i-1):
            if datas[j]>datas[j+1]:
                #交换数据
                temp=datas[j]
                datas[j]=datas[j+1]
                datas[j+1]=temp

l=[2,3,1,4,4,5,6,7,3,2,1,3,5,34,2]
MaoPaoSort(l)
print(l)

class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __str__(self):
        return f"{self.name}:{self.score}"
l=[Student("a",1),
   Student("b",43),
   Student("c",12),
   Student("d",11),
   Student("e",12),
   Student("f",321),
   Student("g",12),
   Student("a",1),
   Student("b",4),
]

MaoPaoSort(l,cmpAttr="score")

for v in l:
    print(v,sep=" ")


