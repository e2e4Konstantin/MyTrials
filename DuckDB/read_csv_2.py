import duckdb
# import csv

csv_file = (
    r"C:\Users\kazak.ke\Documents\Задачи\5_Надя\Результаты\price_materials_report.csv"
)

with duckdb.connect("file.db") as con:

    q = "SELECT * FROM read_csv(?, delim = ';', header = true, decimal_separator = ',');"

    # results = con.execute(q, [csv_file]).fetchall()
    results = con.execute(q, [csv_file]).df()
    print(results)
    print(results.columns.dtype)