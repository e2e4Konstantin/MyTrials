class Divide:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
 
    def __enter__(self):
        print("Inside __enter__")
        return self
 
    def __exit__(self, exc_type, exc_value, traceback):
        print("\nInside __exit__")
        print("\nExecution type:", exc_type)
        print("\nExecution value:", exc_value)
        print("\nTraceback:", traceback)
 
    def divide_by_zero(self):
        # causes ZeroDivisionError exception
        print(self.num1 / self.num2)
 
 
# Driver's code
with Divide(3, 0) as r:
    r.divide_by_zero()