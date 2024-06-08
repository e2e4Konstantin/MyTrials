import duckdb

# cities = [
#     "INSERT INTO Cities VALUES ('NL', 'Amsterdam', 2000, 1005);",
#     "INSERT INTO Cities VALUES ('NL', 'Amsterdam', 2010, 1065);",
#     "INSERT INTO Cities VALUES ('NL', 'Amsterdam', 2020, 1158);",
#     "INSERT INTO Cities VALUES ('US', 'Seattle', 2000, 564);",
#     "INSERT INTO Cities VALUES ('US', 'Seattle', 2010, 608);",
#     "INSERT INTO Cities VALUES ('US', 'Seattle', 2020, 738);",
#     "INSERT INTO Cities VALUES ('US', 'New York City', 2000, 8015);",
#     "INSERT INTO Cities VALUES ('US', 'New York City', 2010, 8175);",
#     "INSERT INTO Cities VALUES ('US', 'New York City', 2020, 8772);",
# ]

# with duckdb.connect("file.db") as con:
#     con.sql("DROP TABLE IF EXISTS Cities;")
#     con.sql("CREATE TABLE Cities (Country VARCHAR, Name VARCHAR, Year INTEGER, Population INTEGER);")
#     for q in cities:
#         con.sql(q)
#     con.table("Cities").show()
#     con.sql("SELECT * FROM Cities").show()

with duckdb.connect("file.db") as con:
    con.sql("SELECT * FROM Cities").show()
    con.sql("PIVOT Cities ON Year USING sum(Population);").show()
    # con.sql("PIVOT Cities ON Population USING sum(Year);").show()
    q = "PIVOT Cities ON Year USING sum(Population) GROUP BY Country;"
    con.sql(q).show()
    q = "PIVOT Cities ON Year IN (2000, 2010) USING sum(Population) GROUP BY Country;"
    con.sql(q).show()
    q = "PIVOT Cities ON Country, Name USING sum(Population);"
    con.sql(q).show()
    q = "PIVOT Cities ON Country || '_' || Name USING sum(Population);"
    con.sql(q).show()
    q = "PIVOT Cities ON Year USING sum(Population) AS total, max(Population) AS max GROUP BY Country;"
    con.sql(q).show()
    q = "PIVOT Cities ON Year USING sum(Population) GROUP BY Country, Name;"
    con.sql(q).show()
    #
    q = """--sql
        WITH pivot_alias AS (
            PIVOT Cities ON Year USING sum(Population) GROUP BY Country
        )
        SELECT * FROM pivot_alias;
    """
    con.sql(q).show()
    # standard sql
    q = """--sql
        FROM Cities
        PIVOT (
            sum(Population)
            FOR
                Year IN (2000, 2010, 2020)
            GROUP BY Country
        );
    """
    con.sql(q).show()
