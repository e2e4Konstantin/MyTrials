import sqlite3
import csv
import os
from icecream import ic
import time
import re

path_name = r"F:\Temp\python_tests"
file_name = r"Статистика_21.csv"                             # r"test.csv"
csv_file = os.path.join(path_name, file_name)
ic(csv_file)



query_create = """CREATE TABLE IF NOT EXISTS tblStatisticsRaw 
        (
            ID_tblStatisticRaw INTEGER PRIMARY KEY NOT NULL, 
            case_num TEXT,
            pressmark TEXT,
            title TEXT,
            uom TEXT,
            volume TEXT,
            card_num TEXT,
            obj_name TEXT,
            activity_type TEXT,
            obj_type TEXT,
            obj_group TEXT,
            examination_date TEXT
        );"""

query_insert = """INSERT INTO tblStatisticsRaw 
                    (
                        case_num, pressmark, title, uom, volume, card_num, obj_name, 
                        activity_type, obj_type, obj_group, examination_date
                    ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    );"""
#
# con = sqlite3.connect('statistics_raw.db')
# con.execute(query_create)
#
# # data_set = []
#
#
# start_time = time.monotonic()
#
# with open(csv_file, 'r', encoding="utf8", newline='') as cf:
#     csv_file_reader = csv.reader(cf, delimiter=';', strict=False)
#     # пропускаем заголовок
#     header = next(csv_file_reader)
#     ic(type(header), len(header))
#     ic(header)
#     ic(type(csv_file_reader))
#     line_count = 0
#     for row in csv_file_reader:
#         # data_set.append(tuple(row))
#         con.execute(query_insert, tuple(row))
#         line_count += 1
#     message = f"из файла {file_name!r} прочитано: {line_count} строк."
#     ic(message)
#
# # con.executemany(query_insert, data_set)
# con.commit()
# con.close()
# elapsed_time = time.monotonic() - start_time
# print(f"время выполнения: {elapsed_time: .5f} секунд.")
#
#
def regex(expression, item):
    reg = re.compile(expression)
    return reg.search(item) is not None

con = sqlite3.connect('statistics_raw.db')
con.create_function("REGEXP", 2, regex)


cursor = con.execute("""select * FROM tblStatisticsRaw WHERE pressmark REGEXP '^[0]+\..*'""")
print(cursor)
print(cursor.lastrowid)

con.commit()
con.close()

# -- SELECT * FROM tblStatisticsRaw WHERE pressmark REGEXP '^[0]+\..*';
#
# -- DELETE FROM tblStatisticsRaw WHERE pressmark in ('0.0-0-0', '00.00-000-0');
#
# DELETE FROM tblStatisticsRaw WHERE pressmark REGEXP '^[0]+\..*';