class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def set_age(self, value):
        self.age = value
    def __str__(self):
        return f"{self.name} {self.age}"

if __name__ == '__main__':
    x = Student('Bob', 88)
    x.set_age(89)
    print(x)
