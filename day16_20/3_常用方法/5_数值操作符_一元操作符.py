class Data:
    def __init__(self,name,f):
        self.name=name
        self.f=f
    #实现取正的操作  +object
    def __pos__(self):
        self.name= f"+{self.name}"
        return self
    #实现取负操作，-object
    def __neg__(self):
        self.name= f"-{self.name}"
        return self
    #实现取绝对值操作，
    def __abs__(self):
        self.name = f"|{self.name}|"
        return self
    #实现取反操作
    def __invert__(self):
        self.name=f"取反{self.name}"
        return self
    #
d=Data("data")
print(d.name)

print((+d).name)
print((-d).name)
print(abs(d).name)