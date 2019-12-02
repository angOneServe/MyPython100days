'''
我的序列，伪战队序列
__len__(self)
返回长度时，是假长度100



'''
class KeyHodeError(Exception):
    def __init__(self,code=101,message="the key are already hold!",args=("值已经存在",)):
        self.args=args
        self.code=code
        self.message=message
class Steam(dict):
    def __init__(self):
        self.dict={}
        self.keys=self.dict.keys()
        self.values=self.dict.values()
    def __len__(self):
        return len(self.keys)
    def __getitem__(self, item):
        return self.dict[item]
    def __setitem__(self, key, value):
        if key not in self.keys:
            self.dict[key]=value
        else:
            e=KeyHodeError()
            #raise e
            print(e)
    def __delitem__(self, key):
        del self.dict[key]

    def __iter__(self):
        return iter(self.keys) #返回keys
    def __instancecheck__(self, instance):
        print("__instancecheck__")
        if instance=="实例":
            return True
        return False
    def __subclasscheck__(self, subclass):
        print("__subclasscheck__")
        return True




s=Steam()
print(len(s))
s["a"]=1
s["a"]=1
s["b"]=2
s["c"]=3
s["d"]=4
s["e"]=5
for k in s:
    print(k,s[k])

class B:
    pass
b=B()
print(isinstance(Steam,s))

#print(issubclass(Steam,B))