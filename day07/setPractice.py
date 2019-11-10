#创建集合set
set1={x for x in range(2,11) if x%2==0}
set2=set([1,2,3,4])
set3=set((1,2,3,4))
print(type(set1))
print(set1)
print(type(set2))
print(set2)
print(type(set3))
print(set3)

#集合的交集 并集 差集
print("交集",set1&set2)
print("交集",set1.intersection(set2))

print("并集",set1|set2)
print("并集",set1.union(set2))

print("差集",set1-set2)
print("差集",set1.difference(set2))

#除去相同元素 set1|set2-set1&set2
print(set1,set2,set1^set2)
print((set1|set2)-(set1&set2))

#判断子集与超集
print(set1>=set2)
print(set2>=set1)
set3=set1&set2
print(set3<=set1)
print(set3.issubset(set1))
print(set3.issubset(set2))
print(set1.issuperset(set3))

print("测试svn")
