class P:
    pass
class C(P):
    pass

print (issubclass(C,P))
print(isinstance(C(),C))