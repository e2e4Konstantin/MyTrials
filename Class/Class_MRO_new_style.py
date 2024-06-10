class Base(object):
    def __init__(self):
        print("-> Base")
        super(Base, self).__init__()
        print("<- Base")


class A(Base):
    def __init__(self):
        print("-> A")
        super(A, self).__init__()
        print("<- A")



class B(Base):
    def __init__(self):
        print("-> B")
        super(B, self).__init__()
        print("<- B")


# a=A()
# b=B()
# print(a.__dict__)
# print(b.__class__.mro())


class C(A):
    def __init__(self):
        print("-> C")
        super(C, self).__init__()
        print("<- C")

class D(B):
    def __init__(self):
        print("-> D")
        super(D, self).__init__()
        print("<- D")


# c=C()
# print(c.__dict__)
# print(c.__class__.mro())
# print()
# d = D()
# print(d.__dict__)
# print(d.__class__.mro())


class E(C, D):
    def __init__(self):
        print("-> E")
        super(E, self).__init__()
        print("<- E")

e=E()
print(e.__dict__)
print(e.__class__.mro())

#         self.e_value = e_value

# print(E.mro())

# # print("MRO:", [cls.__name__ for cls in E.mro()])
# # print("MRO:", [cls.__name__ for cls in D.mro()])

# # c = C(10, 20, 30)
# # print(c.__dict__)
# # d = D(16, 27, 38)
# # print(d.__dict__)

# e = E(10, 20, 30, 40, 50, 60)
# # print(e.__dict__)
