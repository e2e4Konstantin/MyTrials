def add(x, y):
   return x + y
   
def multiply(x, y):
   return x * y
   
def apply_operation(func: callable, x: int, y: int):
   return func(x, y)
   
print(apply_operation(add, 5, 7))   