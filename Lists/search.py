my_list = [10, 20, 30, None, 40, 50]

n = 30
n = None
index = my_list.index(n)
print(f"n: {n}, index: {index}")

items = [(10, 'A'), (20, 'B'), (30, 'C'), (None, 'DD'), (40, 'E'), (50, 'FA')]

target_item = None
index = [i for i, item in enumerate(items) if item[0] == target_item]
print(f"target_item: {target_item}, index: {index}")

print(my_list[1:])