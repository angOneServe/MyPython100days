#c:center  l:left   r:right
def quicklySort(data,L,R):
    #如果l>=r不需要再排序 也是递归退出条件
    if L>=R:
        return

    #确定索引位置
    c=L
    l=L
    r=R

    while r>l:

        #右边寻找比data[c]小的数字
        while data[r]>=data[c] and  r>l:
            #如果l r 位置不重合
            r-=1
        #左边寻找比data[c]大的数字
        while data[l]<=data[c] and r>l :
             #如果l r 位置不重合
            l+=1

        #找到要交换的数据了：
        #左右交换
        if l<r:
            temp=data[l]
            data[l]=data[r]
            data[r]=temp
            print(data)
            continue

    #重合了
    # 由于是r先移动，那么要重合的话，最多就是移到了l位置，而l位置是比c位置小的，因此可以直接将l与c位置的数据交换
    temp=data[l]
    data[l]=data[c]
    data[c]=temp
    print(data)
    c=l
    quicklySort(data,c+1,R)
    quicklySort(data,L,c-1)



#l=[2,3,1,4,4,5,6,7,3,2,1,3,5,34,2]
l=[8,3,1,4,5,6,75,1,1,2,34]
leng=len(l)-1
quicklySort(l,0,leng)
print(l)


