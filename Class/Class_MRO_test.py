class Base:
    def __init__(self, value):
        self.value = value


class A(Base):
    def __init__(self, base_value, a_value):
        Base.__init__(self, base_value)
        self.a_value = a_value


class B(Base):
    def __init__(self, base_value, b_value):
        super().__init__(base_value)
        self.b_value = b_value
# a=A(1,2)
# b=B(1,2)
# print(a.__dict__)
# print(b.__class__.mro())


class C(A):
    def __init__(self, base_value, a_value, c_value):
        print("C: ", locals().keys())
        super().__init__(base_value, a_value)
        self.c_value = c_value

class D(B):
    def __init__(self, base_value, b_value, d_value):
        print("D: ", locals().keys())
        B.__init__(self, base_value=base_value, b_value=b_value)
        self.d_value = d_value

# c=C(1, 2, 3)
# d=D(33, 55, 77)
# print(c.__dict__)
# print(d.__dict__)
# # print(d.__class__.mro())




class E(C, D):
    def __init__(self, base_value, a_value, c_value, b_value, d_value, e_value):
        C.__init__(self, base_value=base_value, a_value=a_value, c_value=c_value)
        D.__init__(self, base_value=base_value, b_value=b_value, d_value=d_value)


        self.e_value = e_value

print(E.mro())

# print("MRO:", [cls.__name__ for cls in E.mro()])
# print("MRO:", [cls.__name__ for cls in D.mro()])

# c = C(10, 20, 30)
# print(c.__dict__)
# d = D(16, 27, 38)
# print(d.__dict__)

e = E(10, 20, 30, 40, 50, 60)
# print(e.__dict__)
