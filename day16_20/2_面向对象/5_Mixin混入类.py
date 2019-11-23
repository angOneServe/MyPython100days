class MydictBase(object):
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key)+"已经存在！！")
        return super().__setitem__(key,value)
class MyDict(MydictBase,dict):
    pass


my_dict=MyDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)
