# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# def print_info(name, age, city):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"City: {city}")

# # Unpack the dictionary and pass the values as keyword arguments
# print_info(**my_dict)

# unpacking
a = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(a)
unpacking = {**a}
print(unpacking)
