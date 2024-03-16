class A:
    def __init__(self, a, **kwargs):
        print('A', a, kwargs)
        self.a = a or None
        self.connect = None
        self.cursor = None
    
    def __enter__(self):
        """ Методы, вызываемые при старте контекстного менеджера.  Объект, возвращаемый данной функцией, 
        присваивается переменной x в конце выражения with as x."""
        print("A:__enter__")
        self.connect = 'connect'
        self.cursor = 'cursor'
        return self.cursor

    def __exit__(self, exception_type, exception_value, traceback):
        """ Будет вызван в завершении конструкции with, или в случае возникновения ошибки после нее.
        В этот метод передаются параметры завершения процесса, а код этого метода будет выполнен гарантированно.
        """
        print("A:__exit__")
        self.connect = None
        self.cursor = None
    
    def __str__(self):
        return f"A: {self.a}, {self.connect}, {self.cursor}"
        
    def foo(self):
        return f"A foo: {self.a}, {self.connect}, {self.cursor}"    
    

class B:

    def __init__(self, a, b, **kwargs):     
        print('B', b, kwargs)
        self.b = b
        self.aa=A(a)
    
    def command(self):
        print("out B: ", self.aa)         
        self.aa.cursor = 111
        with self.aa as aaa:
            print(aaa)
        print("out: ",self.aa.connect, self.aa.cursor)    
            

# a = A(77)
# print(a)       
# with a as x:
    # print(a, a.__dict__)       
# print(a, a.__dict__)     

b = B(88, 66)
b.command()

# print(B.__mro__)
# b = B(77, 999)
# print(vars(b))
# b.command()
