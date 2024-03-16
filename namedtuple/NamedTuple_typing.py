


from typing import NamedTuple


class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee: {self.name!r}, id={self.id}>'


x = Employee('Bob', 5)
print(x)
print(x.name)
