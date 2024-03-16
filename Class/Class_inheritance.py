# # class Parent:
# #     def __init__(self):
# #         self.parent_attribute = 'I am a parent'
# #         print(f'Parent {self.__class__}')
# #
# #     def parent_method(self):
# #         print(f'Back in my day...{self.parent_attribute}')
# #
# #
# # # Create a child class that inherits from Parent
# # class Child(Parent):
# #     def __init__(self):
# #         # Parent.__init__(self)
# #         super().__init__()
# #         self.child_attribute = 'I am a child'
# #         print(f'Child {self.__class__}')
# #
# #
# # # Create instance of child
# # child = Child()
# #
# #
# #
# # # Show attributes and methods of child class
# # print(child.child_attribute)
# # print(child.parent_attribute)
# # child.parent_method()
# #
# #
# # class B:
# #     def x(self):
# #         print('x: B')
# #
# #
# # class C:
# #     def x(self):
# #         print('x: C')
# #
# #
# # class D(B, C):
# #     pass
# #
# #
# # d = D()
# # d.x()
# # print(D.mro())
#
# #
# # class Tokenizer:
# #     """Tokenize text"""
# #     def __init__(self, text):
# #         print('Start Tokenizer.__init__()')
# #         self.tokens = text.split()
# #         print('End Tokenizer.__init__()')
# #
# #
# # class WordCounter(Tokenizer):
# #     """Count words in text"""
# #     def __init__(self, text):
# #         print('Start WordCounter.__init__()')
# #         super().__init__(text)
# #         self.word_count = len(self.tokens)
# #         print('End WordCounter.__init__()')
# #
# #
# # class Vocabulary(Tokenizer):
# #     """Find unique words in text"""
# #     def __init__(self, text):
# #         print('Start init Vocabulary.__init__()')
# #         super().__init__(text)
# #         self.vocab = set(self.tokens)
# #         print('End init Vocabulary.__init__()')
# #
# #
# # class TextDescriber(WordCounter, Vocabulary):
# #     """Describe text with multiple metrics"""
# #     def __init__(self, text):
# #         print('Start init TextDescriber.__init__()')
# #         super().__init__(text)
# #         print('End init TextDescriber.__init__()')
# #
# #
# # td = TextDescriber('row row row your boat')
# # print('--------')
# # print(td.tokens)
# # print(td.vocab)
# # print(td.word_count)
# #
# #
# # # https://python-course.eu/oop/multiple-inheritance.php
# #
# # class A:
# #     def m(self):
# #         print("m of A called")
# # class B(A):
# #     def m(self):
# #         print("m of B called")
# # class C(A):
# #     def m(self):
# #         print("m of C called")
# # class D(B,C):
# #     def m(self):
# #         print("m of D called")
# #
# # class E(B,C):
# #     def m(self):
# #         print("m of D called")
# #         B.m(self)
# #         C.m(self)
# #         A.m(self)
# #
# # # from super1 import A,B,C,D
# # x = D()
# # B.m(x)
# # C.m(x)
# # A.m(x)
# # print()
# # y = E()
# # y.m()
# #
# # from mro import D
# # x = D()
# # x.m()
# #
# # import logging
# # import collections
# # import pprint
# #
# #
# # class LoggingDict(dict):
# #     def __setitem__(self, key, value):
# #         logging.info('Setting %r to %r' % (key, value))
# #         super().__setitem__(key, value)
# #
# #
# # class LoggingOD(LoggingDict, collections.OrderedDict): pass
# #
# # # pprint(LoggingOD.__mro__)
# # print(LoggingOD.mro())
# #
# #
# #
# # class Shape:
# #     def __init__(self, shapename, **kwds):
# #         self.shapename = shapename
# #         super().__init__(**kwds)
# #
# # class ColoredShape(Shape):
# #     def __init__(self, color, **kwds):
# #         self.color = color
# #         super().__init__(**kwds)
# #
# # cs = ColoredShape(color='red', shapename='circle')
#
# class Root:
#     def draw(self):
#         # the delegation chain stops here
#         assert not hasattr(super(), 'draw')
#
#
# class Shape(Root):
#     def __init__(self, shapename, **kwds):
#         self.shapename = shapename
#         super().__init__(**kwds)
#
#     def draw(self):
#         print('Drawing.  Setting shape to:', self.shapename)
#         super().draw()
#
#
# class ColoredShape(Shape):
#     def __init__(self, color, **kwds):
#         self.color = color
#         super().__init__(**kwds)
#
#     def draw(self):
#         print('Drawing.  Setting color to:', self.color)
#         super().draw()
#
#
# cs = ColoredShape(color='blue', shapename='square')
# cs.draw()
#
#
#
#
# position = ColoredShape.__mro__.index
# print(position)

# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/


class A:
    def __init__(self, a, **kwargs):
        if hasattr(self, 'a'):
            return
        print('A', a, kwargs)
        super().__init__(**kwargs)
        self.a = a

class B(A):
    def __init__(self, a, b, **kwargs):
        print('B', b, kwargs)
        super().__init__(a, **kwargs)
        self.b = b

class C(A):
    def __init__(self, a, c, **kwargs):
        print('C', c, kwargs)
        super().__init__(a, **kwargs)
        self.c = c

class D(B, C):
    def __init__(self, a, b, c, d, **kwargs):
        print('D', d, kwargs)
        super().__init__(a=a, b=b, c=c, **kwargs)
        # C.__init__(self, a, c)
        self.d = d

print(D.__mro__)
d = D(1,2,3,4)
print(vars(d))

#---------------------------------------------------------------------

class Base(object):
    def __init__(self, *args, **kwargs): pass

class A(Base):
    def __init__(self, *args, **kwargs):
        print "A"
        super(A, self).__init__(*args, **kwargs)

class B(Base):
    def __init__(self, *args, **kwargs):
        print "B"
        super(B, self).__init__(*args, **kwargs)

class C(A):
    def __init__(self, arg, *args, **kwargs):
        print "C","arg=",arg
        super(C, self).__init__(arg, *args, **kwargs)

class D(B):
    def __init__(self, arg, *args, **kwargs):
        print "D", "arg=",arg
        super(D, self).__init__(arg, *args, **kwargs)

class E(C,D):
    def __init__(self, arg, *args, **kwargs):
        print "E", "arg=",arg
        super(E, self).__init__(arg, *args, **kwargs)

print "MRO:", [x.__name__ for x in E.__mro__]
E(10)
yields

MRO: ['E', 'C', 'A', 'D', 'B', 'Base', 'object']
E arg= 10
C arg= 10
A
D arg= 10
B



!!!!!!!!!! https://realpython.com/python-super/


