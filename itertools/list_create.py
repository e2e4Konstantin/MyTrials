import itertools


max_history_len: int = 10


# n1 = [None] * max_history_len
# print(n1)

n2 = list(itertools.repeat("*", max_history_len))
print(n2)

n2 = [1,3,5,7,9,11]
print(n2[-1])
print(len(n2), n2)
print(n2[-len(n2):])
n2 = n2[:2]
# print(n2)
# print(n2[5:])
# print(n2[len([]):])

# src = ["A", "B", "C"]

# src = src[:max_history_len] if len(src) > max_history_len else src
# print(src)

# r = n2[len(src):] + src
# print(r)