import blaze
from collections import Iterator, Iterable



t = blaze.data([(1, 'Alice', 100),
           (2, 'Bob', -200),
           (3, 'Charlie', 300),
           (4, 'Denis', 400),
           (5, 'Edith', -500)],
        fields=['id', 'name', 'balance'])

# print(t.peek())

from blaze.utils import example
iris = blaze.data(example('iris.csv'))
iris.peek()