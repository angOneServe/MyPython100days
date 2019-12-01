class Test:
    def __init__(self,name):
        self.name=name
    #返回True表示相等，返回Fasle表示不相等
    def __eq__(self, other):
        if len(self.name) == len(other.name):
            return True
        return False

    # 不等于
    def __ne__(self, other):
        if len(self.name) !=len(other.name):
            return True
        return False
    #大于
    def __gt__(self, other):
        if len(self.name) >len(other.name):
            return True
        return False
    # 小于
    def __lt__(self, other):
        if len(self.name) < len(other.name):
            return True
        return False
    #大于等于
    def __ge__(self, other):
        if len(self.name) >= len(other.name):
            return True
        return False
    #小于等于
    def __le__(self, other):
        if len(self.name) <= len(other.name):
            return True
        return False



t1=Test("大")
t2=Test("dd")
t3=Test("等于")
print(t1==t2)
print(t3==t2)


l=[Test("fdaad"),Test("fdad"),Test("fadafed"),Test("fadae"),Test("fd"),Test("faaedsdadsasd")]
l.sort()
for v in l:
    print(v.name,end=" ")

#############################################################################
#python3取消了__cmp__,增加了
'''
# 返回负整数，self<other
    # 返回0，self==other
    # 返回正整数，self>other
    def __cmp__(self, other):
        if len(self.name) > len(other.name):
            return 1
        elif len(self.name) < len(other.name):
            return -1
        else:
            return 0
'''