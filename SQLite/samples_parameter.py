import pyodbc
import pandas as pd
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\sqlexpress;'
                      'Database=DBname;'
              'UID=myuserid'
              'PWD=mypassword;')
crsr = cnxn.cursor()

sql="Select Top 5 * from mytable where id between ? and ?"
df = pd.read_sql(sql,cnxn,params =[52,65])
df

f = pd.read_sql_query('SELECT open FROM NYSEMSFT WHERE date = (?)', conn, params=(date,))


print("this is print")
s ="trrhhh"

curs.execute(
    "SELECT weight FROM Equipment WHERE name = :name AND price = :price",
    {"name": "lead", "price": 24},
)

curs.execute(
    "SELECT weight FROM Equipment WHERE name = ? AND price = ?",
    ["lead", 24],
)


import sqlite3
import pandas as pd
con = sqlite3.connect("test.db")
with con:
    df = pd.read_sql("select * from Movie", con)
print(df)

Lockedlist_panda = Lockedlist_panda[["NR","Programme","Sub_Region","Site_Type","MS13_Actual" ]]
