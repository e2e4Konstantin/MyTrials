import sqlite3
import os
import pandas as pd

print(sqlite3.version)
print(sqlite3.sqlite_version)

db_name = os.path.join(os.path.dirname(__file__), "aw.sqlite3")
src_data = os.path.join(os.path.dirname(__file__), "Data\DimCustomer.csv")


conn = sqlite3.connect(db_name)
conn.execute("DROP TABLE IF EXISTS customer;")
conn.execute(
    """
             CREATE TABLE customer (
                CustomerKey INTEGER PRIMARY KEY NOT NULL,
                LastName TEXT,
                BirthDate TEXT,
                MaritalStatus TEXT,
                YearlyIncome REAL,
                ModifiedDate TEXT,
                ETLLastUpdate DATETIME DEFAULT CURRENT_TIMESTAMP
             );
             """
)

print(pd.read_sql_query(
    "select name from sqlite_master where type = 'table'", conn
    ))

df = pd.read_csv(src_data, index_col=False)
print(df)
print(df.columns)
print(df.dtypes)

df.to_sql('customer', conn, if_exists='append', index=False)

x = pd.read_sql_query(sql="select * from customer", con=conn)
print(x)


x = pd.read_sql_query(sql="PRAGMA table_info('customer');", con=conn)
print(x)

# conn.commit()
conn.close()
