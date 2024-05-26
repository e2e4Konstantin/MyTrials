# a = 6
# match a:
    # case 1:
        # print('1')
    # case 5:
        # print('5')
    # case _:
        # print('***')


# day = "Monday"
# switch day {
  # case "Sunday"   : print("Take it easy")
  # case "Monday"   : print("Go to work")
  # case "Tuesday"  : print("Work + Hobbies")
  # case "Wednesday": print("Meetings")
  # case "Thursday" : print("Presentations")
  # case "Friday"   : print("Interviews and party")
  # case "Saturday" : print("Time to do sports")}


  # match day:
    # case "Sunday"    : print("Take it easy")
    # case "Monday"    : print("Go to work")
    # case "Tuesday"   : print("Work + Hobbies")
    # case "Wednesday" : print("Meetings")
    # case "Thursday"  : print("Presentations")
    # case "Friday"    : print("Interviews and party")
    # case "Saturday"  : print("Time to do sports")
# name = "Jack"
# match name:
        # # Check if name == None
        # case None:
            # print("Hello there")
        # # Store name into some_name if it is not None
        # case some_name:
            # print(f"Hello {some_name}")
#
#
# match numbers:
#     case int() | float() as num:
#         print(f'число: {num}')
#     case str() as num if num.isdigit():
#         print(f"стало целое число: {int(num)}")
#     case str() as num if num.replace(',', '', 1).replace('.', '', 1).isdigit():
#         print(f'строка: "{num}" стала числом: {float(num.replace(",", ".", 1))}')
#     case _:
#         print(f'непонятно {numbers}')
#
#
#
# f = lambda x: x is None
#
# name = None
# match name:
#     case "Jack":
#         print("Hello Jack")
#     case f:
#         print("Hello None")
#     case _:
#         print(f"Hello Anyone")
#
#
#
#
# numbers = '125,55'
# # numbers = 125.55
#
#
# match numbers:
#     case int() | float() as num:
#         print(f'число: {num}')
#     case str() as num if len(set('.,').intersection(num)) == 1:
#         print(f'строка: "{num}" стала числом: {float(num.replace(",", ".", 1))}')
#     case _:
#         print('непонятно')

name = "Jack8"
match name:
        # Check if name == None
        case None:
            print("Hello there")
        # Store name into some_name if it is not None
        case some_name if len(some_name) == 4:
            print(f"Hello {some_name}")
        case _:
            print('непонятно')

name = "Jack"
match name:
        case name_ if len(name_) == 4:
            print(f"Hello {name_}")
        case _:
            print('непонятно')
