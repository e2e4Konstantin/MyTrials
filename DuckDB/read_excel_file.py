# https://hakibenita.com/fast-excel-python
import duckdb
from typing import IO, Iterator

def iter_excel_duckdb(file: IO[bytes]) -> Iterator[dict[str, object]]:
    duckdb.install_extension('spatial')
    duckdb.load_extension('spatial')
    rows = duckdb.sql(f"""
        SELECT * FROM st_read(
            '{file.name}',
            open_options=['HEADERS=FORCE', 'FIELD_TYPES=AUTO'])
    """)
    while row := rows.fetchone():
        yield dict(zip(rows.columns, row))


excel_file = (
        r"C:\Users\kazak.ke\Documents\PythonProjects\UPSS\TryOut\Шаблон_формы_N.xlsx"
    )
sheet_name = "test"

with open(excel_file, 'rb') as f:
    rows = iter_excel_duckdb(f)
    row = next(rows)
    print(row)