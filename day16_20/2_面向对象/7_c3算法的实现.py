'''
mro即 method resolution order (方法解释顺序)

merge:
C3算法
判断mro要先确定一个线性序列，然后查找路径由由序列中类的顺序决定。所以C3算法就是生成一个线性序列。
如果继承至一个基类:
class B(A)
这时B的mro序列为[B,A]

如果继承至多个基类
class B(A1,A2,A3 ...)
这时B的mro序列 mro(B) = [B] + merge(mro(A1), mro(A2), mro(A3) ..., [A1,A2,A3])
merge操作就是C3算法的核心。
遍历执行merge操作的序列，如果一个序列的第一个元素，是其他序列中的第一个元素，或不在其他序列出现，则从所有执行merge操作序列中删除这个元素，合并到当前的mro中。
merge操作后的序列，继续执行merge操作，直到merge操作的序列为空。
如果merge操作的序列无法为空，则说明不合法。


c3实现思路
遍历所以列表对象，

'''
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

#得到准备合并的列表
def GetList(cl):
    bases=cl.__bases__
    bases=list(bases)
    print(len(bases))
    if  len(bases)==0: #object
        return list(cl,)
    elif len(bases)==1 and bases[0]==object:
        return [cl,object]
    else:
        temps=[]
        for v in bases:
            t=GetList(v)
            temps.append(t)
        bases.append(cl)
        temps.append(bases)
        return temps





#计算某个类的Mro
def Mro(cl):
    #得到所有基类
    cls=GetList(cl)
    cls.insert(0,cl)    #将自己插入列表
    if cls.count()<=2:  # 是object或只有object一个基类,不需要再去找基类了,直接返回列表
        return cls
    else:               #基类上还有基类【非object】
        clsList=[]
        cls.append(cls)
        for childClass in cls:
            clsList.append(Mro(childClass))

        cls=MyMerge(clsList)
        return cls

#合并所有列表
def MyMerge(*itemList):
    pass
    #for l in itemList:


#他人算法
#-*- encoding:GBK -*-#
def mro_C3(*cls):
        if len(cls)==1:
            #if not cls[0].__bases__:#只有一个类，且无父类   ----返回自身
            if cls[0].__bases__ is None:
                #print("类型1", type(cls ), cls[0].__bases__)
                return  cls
            else:                   #只有一个类，且有父类   ----返回自身+mro(父类)
                #print("类型2",type(cls+ mro_C3(*cls[0].__bases__)),cls[0].__bases__)
                return cls+ mro_C3(*cls[0].__bases__)
        else:                       #列表中非只有一个类,对每个类求mro，最后加上自身列表
            #seqs = [list(mro_C3(C)) for C in cls ] +[list(cls)]#遍历
            seqs =[list(cls)]+[list(mro_C3(C)) for C in cls]   # 遍历
            #print("seqs",seqs)
            res = []
            while True:
              non_empty = list(filter(None, seqs))
              if not non_empty:
                  return tuple(res)
              for seq in non_empty:
                  candidate = seq[0]
                  not_head = [s for s in non_empty if candidate in s[1:]]
                  if not_head:
                      candidate = None
                  else:
                      break
              if not candidate:
                  raise TypeError("inconsistent hierarchy, no C3 MRO is possible")
              res.append(candidate)
              for seq in non_empty:
                  if seq[0] == candidate:
                      del seq[0]

print(mro_C3(D))
print(GetList(D))