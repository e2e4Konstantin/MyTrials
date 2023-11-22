# https://dagster.io/blog/duckdb-data-lake#-the-limitations-of-duckdb

import pandas


class SQL:
    def __init__(self, sql, **bindings):
        self.sql = sql
        self.bindings = bindings


df = pandas.DataFrame()

x = SQL("select * from $df", df=df)
print(x.bindings)
print(f"{x.sql=}")
