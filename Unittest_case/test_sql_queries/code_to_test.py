# code_to_test.py

import sqlite3
import pandas as pd


def function_to_tets():
    df = None
    try:
        db_connect = sqlite3.connect("address_zip.db")
        db_cur = db_connect.cursor()
        db_cur.execute(""" Select STD_ADDRESS,STD_CITY,STD_STATE from address""")
        sql_result = pd.read_sql_query(""" Select STD_ADDRESS,STD_CITY,STD_STATE from address""", db_connect)
        df = pd.DataFrame(sql_result, columns=['STD_ADDRESS', 'STD_CITY', 'STD_STATE'])
        print(f"The data from database is :\n {df}")
        db_cur.close()
        db_connect.close()
    except Exception as e:
        print(f"DB exception: {e}")

    return df