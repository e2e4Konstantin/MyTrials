


# class Base(object):
#     def __init__(self, *args, **kwargs): pass

# class A(Base):
#     def __init__(self, *args, **kwargs):
#         print("A")
#         super(A, self).__init__(*args, **kwargs)

# class B(Base):
#     def __init__(self, *args, **kwargs):
#         print("B")
#         super(B, self).__init__(*args, **kwargs)

# class C(A):
#     def __init__(self, arg, *args, **kwargs):
#         print ("C","arg=", arg)
#         super(C, self).__init__(arg, *args, **kwargs)

# class D(B):
#     def __init__(self, arg, *args, **kwargs):
#         print ("D", "arg=", arg)
#         super(D, self).__init__(arg, *args, **kwargs)

# class E(C,D):
#     def __init__(self, arg, *args, **kwargs):
#         print ("E", "arg=", arg)
#         super(E, self).__init__(arg, *args, **kwargs)

# print("MRO:", [x.__name__ for x in E.__mro__])
# print("MRO:", [x.__name__ for x in D.__mro__])


class A:
    def __init__(self):
        print("A.__init__")


class B:
    def __init__(self):
        print("B.__init__")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C.__init__")
        super().__init__()
        


c = C()