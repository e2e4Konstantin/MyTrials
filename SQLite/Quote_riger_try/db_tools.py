import sqlite3
from icecream import ic

from db import sql_select

print(sqlite3.version)
print(sqlite3.sqlite_version)

db_name = r"F:\Temp\python_tests\t1.sqlite3"
ic(db_name)

# src_data = r" F:\Kazak\GoogleDrive\Python_projects\Quotes_PEM\tests\WORK_PROCESS_67.csv"
# ic(src_data)

# df = pd.read_csv(src_data, delimiter=";", index_col=False, encoding="utf8")
# ic(df)
# # df.apply(lambda x: pd.api.types.infer_dtype(x.values))
# print(df.columns)
# print(df.dtypes)

# conn = sqlite3.connect(db_name)
# conn.execute("DROP TABLE IF EXISTS tblRawQuotes;")
# df.to_sql('tblRawQuotes', conn, if_exists='append', index=False)

# conn.commit()
# conn.close()

conn = sqlite3.connect(db_name)
df = pd.read_sql_query(sql="SELECT * FROM tblRawQuotes;", con=conn)
# # for row in df.itertuples(index=False):
# #     ic(row.PRESSMARK)

raw_data = df.iloc[0]
data = (
    67,
    raw_data.PRESSMARK,
    f"{raw_data.PRESSMARK}-99",
    raw_data.TITLE,
    raw_data.UNIT_OF_MEASURE,
    "parent_quotes",
    0,
    0,
)
ic(data)
conn.execute(sql_select["insert_quote"], data)
# conn.execute("SELECT * FROM tblQuotes;")

conn.commit()
conn.close()
