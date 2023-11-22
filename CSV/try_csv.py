# https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python/

import csv
import os
from icecream import ic

path_name = r"F:\Temp\python_tests"
file_name = r"test.csv"
csv_file = os.path.join(path_name, file_name)
ic(csv_file)

# with open(csv_file, 'r', encoding="utf8", newline='') as cf:
#     csv_file_reader = csv.reader(cf, delimiter=';', strict=False)
#     ic(type(csv_file_reader))
#     line_count = 0
#     for row in csv_file_reader:
#         if line_count == 0:
#             print(f'Column names are: {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

fields = ['CASE_NUM',
          'PRESSMARK',
          'TITLE',
          'UOM',
          'VOLUME',
          'CARD_NUM',
          'OBJ_NAME',
          'ACTIVITY_TYPE',
          'OBJ_TYPE',
          'OBJ_GROUP',
          'EXAMINATION_DATE']

with open(csv_file, 'r', encoding="utf8", newline='') as cf:
    fieldTypes = {}
    csv_reader = csv.DictReader(cf, delimiter=';', strict=False)
    ic(csv_reader.fieldnames)

    line_count = 0
    for row in csv_reader:
        print(f'\t{row}')
        line_count += 1
    print(f'Processed {line_count} lines.')
