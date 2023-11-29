# https://duckdb.org/docs/api/python/overview.html
# https://duckdb.org/2021/05/14/sql-on-pandas.html

import pandas as pd
import numpy as np
import duckdb

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

df1 = pd.DataFrame(
    {"A": ["foo", "bar", "baz", "bat"], "E": ["apple", "orange", "banana", "grape"]}
)

duckdb.sql("SELECT 42").show()
r1 = duckdb.sql("SELECT 42 AS i")
duckdb.sql("SELECT i * 2 AS k FROM r1").show()

# duckdb.read_csv("example.csv")                # read a CSV file into a Relation
# duckdb.read_parquet("example.parquet")        # read a Parquet file into a Relation
# duckdb.read_json("example.json")              # read a JSON file into a Relation

# duckdb.sql("SELECT * FROM 'example.csv'")     # directly query a CSV file
# duckdb.sql("SELECT * FROM 'example.parquet'") # directly query a Parquet file
# duckdb.sql("SELECT * FROM 'example.json'")


res = duckdb.sql("SELECT * FROM df")
res.show()

query = """SELECT A, AVG(D) FROM df GROUP BY A"""
duckdb.sql(query).show()

duckdb.sql("SELECT df.A, df.B, df1.E FROM df JOIN df1 ON df.A = df1.A").show()


duckdb.sql("SELECT 42").fetchall()  # Python objects
duckdb.sql("SELECT 42").df()  # Pandas DataFrame

con = duckdb.connect()
con.sql("SELECT 42 AS x").show()


# # create a connection to a file called 'file.db'
# con = duckdb.connect("file.db")
# # create a table and load data into it
# con.sql("CREATE TABLE test (i INTEGER)")
# con.sql("INSERT INTO test VALUES (42)")
# # query the table
# con.table("test").show()
# # explicitly close the connection
# con.close()
# # Note: connections also closed implicitly when they go out of scope

with duckdb.connect("file.db") as con:
    con.sql("CREATE TABLE test (i INTEGER)")
    con.sql("INSERT INTO test VALUES (42)")
    con.table("test").show()

results = duckdb.sql("SELECT 42").fetchall()
print(results)

results = duckdb.sql("SELECT 42").df()
print(results)


print(duckdb.query("SELECT SUM(C) FROM df").to_df())
