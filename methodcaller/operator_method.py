from operator import methodcaller

names: list[str] = ['Bob', 'James', 'Billy', 'Sandra', 'Black']

starts_with_b = methodcaller('startswith', 'B')
filter_names = filter(starts_with_b, names)
print(list(filter_names))


