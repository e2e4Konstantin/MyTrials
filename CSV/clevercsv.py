
import clevercsv
import os
from icecream import ic

path_name = r"F:\Temp\python_tests"
file_name = r"test.csv"
csv_file = os.path.join(path_name, file_name)
ic(csv_file)

rows = clevercsv.read_table('./imdb.csv')


# with open(csv_file, "r", newline="", encoding="utf-8") as fp:
#     reader = clevercsv.reader(fp, delimiter=";", quotechar="", escapechar="\\")
#     rows = list(reader)

with open(csv_file, "r", newline="") as fp:

  dialect = clevercsv.Sniffer().sniff(fp.read(), verbose=False)
  fp.seek(0)
  reader = clevercsv.reader(fp, dialect)
  rows = list(reader)