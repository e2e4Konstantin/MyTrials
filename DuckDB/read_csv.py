import duckdb

file = r"""F:\Kazak\GoogleDrive\Python_projects\Kat_report_monitoring\report_monitoring.csv"""

read_query = f"CREATE TABLE tblPrices AS SELECT * FROM read_csv('{file}', delim = ';', header = true, AUTO_DETECT=TRUE, types = {'202' : 'INTEGER'});"

with duckdb.connect("file.db") as con:
    con.sql("DROP TABLE IF EXISTS tblPrices;")
    #
    con.sql(read_query)
    # con.sql('ALTER TABLE tblPrices ALTER "202" TYPE INTEGER;')
    con.table("tblPrices").show()


