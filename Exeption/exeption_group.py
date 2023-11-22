# https://docs.python.org/3.11/library/exceptions.html#TypeError
# https://realpython.com/python311-exception-groups/

# try:
#     raise ExceptionGroup('Example ExceptionGroup', (
#         TypeError('Example TypeError'),
#         ValueError('Example ValueError'),
#         KeyError('Example KeyError'),
#         AttributeError('Example AttributeError')
#     ))
# except* TypeError:
#     print('***')
#     rollbar.report_exc_info()
# except* ValueError as e:
#     ...
# except* (KeyError, AttributeError) as e:
#     ...


print(issubclass(ExceptionGroup, Exception))
print(ExceptionGroup("one error", [ValueError(654)]))
print(ExceptionGroup("two errors", [ValueError(654), TypeError("int")]))
eg = ExceptionGroup("nested", [ ValueError(654), ExceptionGroup("imports", [ImportError("no_such_module"), ModuleNotFoundError("another_module"),]),])
print(eg)
# print(ExceptionGroup("no errors", []))

# raise ExceptionGroup("nested",
#     [
#         ValueError(654),
#         ExceptionGroup("imports",
#             [
#                 ImportError("no_such_module"),
#                 ModuleNotFoundError("another_module"),
#             ]
#         ),
#         TypeError("int"),
#     ]
# )


# try:
#     raise ExceptionGroup("group", [ValueError(654)])
# except ExceptionGroup:
#     print("Handling ExceptionGroup")


# try:
#     raise ExceptionGroup("group", [ValueError(654)])
# except ValueError:
#     print("Handling ValueError")

#
try:
    raise ExceptionGroup("group", [ValueError(654)])
except ExceptionGroup as eg:
    for err in eg.exceptions:
        if isinstance(err, ValueError):
            print("Handling ValueError")
        elif isinstance(err, TypeError):
            print("Handling TypeError")

try:
    raise ExceptionGroup("group", [ValueError(654)])
except* ValueError:
    print("Handling ValueError")
except* TypeError:
    print("Handling TypeError")

print(f"{'-'*20}")

try:
    raise ExceptionGroup(
        "group", [TypeError("str"), ValueError(654), TypeError("int")]
    )
except* ValueError as eg:
    print(f"Handling ValueError: {eg.exceptions}")
except* TypeError as eg:
    print(f"Handling TypeError: {eg.exceptions}")

print(f"{'-'*40}")
#
# try:
#     raise ExceptionGroup(
#         "group", [TypeError("str"), ValueError(654), TypeError("int")]
#     )
# except* ValueError as eg:
#     print(f"Handling ValueError: {eg.exceptions}")

eg = ExceptionGroup("group", [TypeError("str"), ValueError(654), TypeError("int")])
print(eg)
value_errors, eg = eg.split(ValueError)
print(value_errors, eg)

import_errors, eg = eg.split(ImportError)
print(import_errors, eg)


try:
    raise ValueError(654)
except* ValueError as eg:
    print(type(eg), eg.exceptions)





