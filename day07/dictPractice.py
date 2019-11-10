#创建字典
d1={1:2,"2":3,"分":"梨"}
print(d1)

d2=dict(one=1,w=3)
print(d2)

d3={x:x*x for x in range(0,12) if x%2==0}
print(d3)

#操作字典
print(d1[1])
print(d1["分"])

d1["分"]="苹果"
print(d1["分"])

d1["吃"]="西瓜"
print(d1["吃"])

d1.pop("吃")
#print(d1["吃"]) #报错

print(d1)
d1.popitem()
print(d1)

d1.clear()
print(d1)
