from functools import total_ordering
@total_ordering
class Test:
    def __init__(self,name):
        self.name=name
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

#因为@tatal__ordering存在，即是没有重写__le__方法也可以比较
#用了@tatal__ordering,至少写一个==或！= 加上 <  >  <= >=其中一个，总共两个方法
print(Test("dd")<=Test("we"))

#cmp为python的，返回正整数则大于，0则等于，返回负整数则小于

