import xlwings as xw
import pandas as pd
import os

path =os.path.dirname(os.path.realpath(__file__))
print(path)
file = os.path.join(path, "Book1.xlsx")
sheet_name = 'test'


wb = xw.Book()

sht = wb.sheets.add(sheet_name)


wb.save(file)

book = xw.Book(file)
sht = book.sheets["test"]
# # sheet = book.sheets["template"].copy(name="report")
# # df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
# # sheet.render_template(df=df)



df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
sht["A1"].value = df
sht["A1"].options(pd.DataFrame, expand="table").value

sht["A1"].expand().font.name = "JetBrains Mono"

sht.cells(5, 5).value = "test"
sht.range("A3:A26").api.Font.Size = 25

my_range = sht.range((5, 5), (9, 9))
my_range.color = (255, 255, 255)
my_range.value = 1


sht.cells(10, 10).value = df

sht.range("A15").color = None
print(sht.range("A15").color is None)

wb.save(file)