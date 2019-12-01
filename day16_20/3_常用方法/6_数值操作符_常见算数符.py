class Data:
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2

    # 加
    def __add__(self, other):
        return self.data2+other.data1

    def __sub__(self, other):
        return self.data2 -other.data1

    def __mul__(self, other):
        return self.data2*other.data1
    #   //
    def __floordiv__(self, other):
        return self.data2 //other.data1
    #   /
    def __truediv__(self, other):
        return self.data2 / other.data1

    def __radd__(self, other):
        return self.data1+other.data

class Data2:
    def __init__(self,data):
        self.data=data

d1=Data(1,2)
d2=Data(3,4)
print(d1+d2)
print(d1-d2)
print(d1*d2)
print(d1//d2)#
print(d1/d2)

#反射运算符，与普通的相比，
#普通的add，参数为运算符左边才会调用
#反射的radd，参数在运算符右边是被调用，且左边这个参数要没有普通的add函数
print(Data2(3)+Data(1,2))

#其他还有
"""
__iadd__(self, other)
实现加法赋值操作。

__isub__(self, other)
实现减法赋值操作。

__imul__(self, other)
实现乘法赋值操作。

__ifloordiv__(self, other)
实现使用 //= 操作符的整数除法赋值操作。

__idiv__(self, other)
实现使用 /= 操作符的除法赋值操作。

__itruediv__(self, other)
实现 _true_ 除法赋值操作，这个函数只有使用 from __future__ import division 时才有作用。

__imod__(self, other)
实现 %= 取余赋值操作。

__ipow__
实现 **= 操作。

__ilshift__(self, other)
实现左移位赋值运算符 <<= 。

__irshift__(self, other)
实现右移位赋值运算符 >>= 。

__iand__(self, other)
实现按位与运算符 &= 。

__ior__(self, other)
实现按位或赋值运算符 | 。

__ixor__(self, other)
实现按位异或赋值运算符 ^= 。
"""