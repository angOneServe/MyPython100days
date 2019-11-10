#python list 浅复制(后续再看，)
l1=[[]]*5
print(l1)
print(id(l1[0]),id(l1[1]),id(l1[2]),id(l1[3]),id(l1[4]))
l1[0]=1
l1[1]=2
print(id(l1[0]),id(l1[1]),id(l1[2]),id(l1[3]),id(l1[4]))
print(l1)

