import sqlite3
import openpyxl

con = sqlite3.connect('test.db')
wb = openpyxl.load_workbook(filename=r'TABLES_ALL_68.xlsx')

sheets = wb.sheetnames

query = """ CREATE TABLE tblOne (ID INTEGER PRIMARY KEY, code TEXT, title TEXT); """
con.execute(query)

for sheet in sheets:
    ws = wb[sheet]

    # tup = []
    for i, rows in enumerate(ws):
        # tuprow = []
        # if i == 0:
        #     continue
        for row in rows:
            v = row.value.strip().decode('utf-8', 'ignore')
            print(v)

    # con.executemany(insQuery, tup)
    # con.commit()

con.close()

#city = 'Ribeir\xc3\xa3o Preto'
# print city.decode('cp1252').encode('utf-8')

# https://stackoverflow.com/questions/4182603/how-to-convert-a-string-to-utf-8-in-python