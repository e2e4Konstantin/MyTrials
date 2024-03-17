a_set: set[int] = {1, 2, 3, 4, 5}
b_set: set[int] = {4, 5, 6, 7, 8}

s_set: set[int] = a_set | b_set # set.union(other, ...) или set | other | - объединение нескольких множеств.
d_set: set[int] = a_set - b_set #
print(s_set, d_set)


print(a_set & b_set) # set.intersection(other, ...) или set & other & - пересечение.
print(a_set ^ b_set) # set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
