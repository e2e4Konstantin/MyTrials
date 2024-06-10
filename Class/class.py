#
# class A(object):
#     @classmethod
#     def do_your_stuff(cls):
#         print('This is A')
#
# class B(A):
#     @classmethod
#     def do_your_stuff(cls):
#         print('This is B')
#         super(B, cls).do_your_stuff()  # CORRECT
#         # super(cls, cls).do_your_stuff()  # WRONG
#
# class C(B):
#     @classmethod
#     def do_your_stuff(cls):
#         print('This is C')
#         super(C, cls).do_your_stuff()  # CORRECT
#         # super(cls, cls).do_your_stuff()  # WRONG
#
# C.do_your_stuff()

#
# class MyClass1:
#     """ Это строка документирования """
#     print("Инструкции выполняются сразу")
#
# class B:
#     n = 5
#
#     def adder(v):
#         return v + B.n
#
# print(B.n)  # Вывод: 5
# print(B.adder(4))  # Вывод: 9
#
# class MyClass:
#     x = 50 # Создаем атрибут объекта класса MyClass
#     def out(self):
#         print(self.__class__)
#
# c1, с2 = MyClass(), MyClass() # Создаем два экземпляра класса
# c1.y = 10 # Создаем атрибут экземпляра класса c1
# с2.ee = 20 # Создаем атрибут экземпляра класса c2
# print(c1.x, ' ', c1.y) # Вывод: 50 10
# print(с2.x, ' ', с2.ee) # Вывод: 50 20
#
# c1.out()
# MyClass.out(c1)
#
# class MyClass:
#     def __init__(self):  # Конструктор
#         self.x = 1  # Атрибут экземпляра класса
#
#     def print_x(self):  # self — это ссылка на экземпляр класса
#         print(self.x)  # Выводим значение атрибута
#
#     def __str__(self):
#         return f'MeClass -> {self.x}'
#
#
# c = MyClass()  # Создание экземпляра класса
# print(c.x)
# c.print_x()
#
# MyClass.print_x(c)
# print(c)
#
#
# class Class1:  # Базовый класс
#     def __init__(self):
#         print("-1 Конструктор базового класса Class 1", self.__class__)
#
#
# class Class2:
#     def __init__(self):
#         print("--2 Конструктор производного класса Class 2", self.__class__)
#
#
# class Class3(Class1, Class2):
#     def __init__(self):
#         print("--3 Конструктор производного класса Class 3", self.__class__)
#         Class1.__init__(self)
#         Class2.__init__(self)
#
#
# c = Class3()
# print(Class3.mro())

#
# import datetime
# today = datetime.date.today()
#
# print(str(today), today, repr(today))
# print(dir(datetime))

#
# class First(object):
#     def __init__(self):
#         print ("First(): entering")
#         super(First, self).__init__()
#         print ("First(): exiting")
#
# class Second(object):
#     def __init__(self):
#         print ("Second(): entering")
#         super(Second, self).__init__()
#         print ("Second(): exiting")
#
# class Third(First, Second):
#     def __init__(self):
#         print ("Third(): entering")
#         super(Third, self).__init__()
#         print ("Third(): exiting")
#
# c =Third()
# print(Third.mro())
#
# class A:
#     def __init__(self, a="a"):
#         self.a = a
#         print(f"A = {a}")
#
#     def A_method(self):
#         print(f"A_method: {self.a}")
#
#
# class B:
#     def __init__(self, b="b"):
#         self.b = b
#         print(f"B = {b}")
#
#     def B_method(self):
#         print(f"B_method: {self.b}")
#
#     def magical_AB_method(self):
#         print(f"magical_AB_method: {self.a}, {self.b}")
#
#
# class AB(A, B):
#     def __init__(self, a="A", b="B"):
#         # super().__init__(a=a, b=b) # fails!
#         A.__init__(self, a=a)
#         B.__init__(self, b=b)
#         self.A_method()
#         self.B_method()
#         self.magical_AB_method()
#
# c1 = A()
# c2 = B()
# c3= AB()
#
#
# #
# #     A
# #    / \
# #   B   C
# #    \ /
# #     D
#
#
# class A:
#     def __init__(self, name=None):
#         #  this is the head of the diamond, no need to call super() here
#         self.name = name
#
# class B(A):
#     def __init__(self, param1='hello', **kwargs):
#         super().__init__(**kwargs)
#         self.param1 = param1
#
# class C(A):
#     def __init__(self, param2='bye', **kwargs):
#         super().__init__(**kwargs)
#         self.param2 = param2
#
# class D(B, C):
#     def __init__(self, works='fine', **kwargs):
#         super().__init__(**kwargs)
#         print(f"{works=}, {self.param1=}, {self.param2=}, {self.name=}")
#
# print()
# d = D(name='Testing')
# print(D.mro())

# https://www.datacamp.com/tutorial/super-multiple-inheritance-diamond-problem

# class Class_A:
#     def __init__(self, name=None):
#         self.name = name
#         print(f"Class_A = {self.name}, {self.__class__}")


# class Class_B(Class_A):
#     def __init__(self, param1='hello', **kwargs):
#         super().__init__(**kwargs)
#         self.param1 = param1
#         print(f"--Class_B = {self.param1}, {self.__class__}")


# class Class_C(Class_A):
#     def __init__(self, param2='bye', **kwargs):
#         super().__init__(**kwargs)
#         self.param2 = param2
#         print(f"--Class_C = {self.param2}, {self.__class__}")


# class Class_D(Class_B, Class_C):
#     def __init__(self, works='fine', **kwargs):
#         super().__init__(**kwargs)
#         print(f"{works=}, {self.param1=}, {self.param2=}, {self.name=}")


# print()
# d = Class_D(name='Testing')
# print(Class_D.mro())



# class AMix:
#     def __init__(self, a, **kwargs):
#         super().__init__(**kwargs)
#         self.a = a


# class BMix:
#     def __init__(self, b, **kwargs):
#         super().__init__(**kwargs)
#         self.b = b


# class AB(AMix, BMix):
#     def __init__(self, a, b):
#         super().__init__(a=a, b=b)


# ab = AB('a1', 'b2')

# print(ab.a, ab.b)  # -> a1 b2

class A:
    def __init__(self, a):
        super().__init__()
        self.a = a

class B(A):
    def __init__(self, a, b):
        super().__init__(self, a)
        self.b = b

class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.c = c

class D(B, C):
    def __init__(self, a, b, c, dd):
        B.__init__(self, a, b)
        C.__init__(self, a, c)
        self.d = dd

d = D(1, 2, 3, 4)
print(d.__class__.mro())
print(d.a)