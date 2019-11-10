row=int(input("请输入行数:"))
nums=[]
for x in range(1,row+1):
    if x==1:
        nums.append([1])
    else:
        temp=[]
        for index in range(x):
            if index==0 or index==x-1:
                temp.append(1)
            else:
                temp.append(nums[x-2][index-1]+nums[x-2][index])
        nums.append(temp)
for v in nums:
    print()
    for y in v:
        print(y,end=",")#去掉回车符
