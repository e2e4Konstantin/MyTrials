import xlwings as xw
import pandas as pd
import os

path =os.path.dirname(os.path.realpath(__file__))
print(path)
file = os.path.join(path, "Book1.xlsx")
sheet_name = 'test'

# print(xw.apps)
# print(xw.App().version)
# with xw.App() as app:
#     print(app.books)

# wb = xw.Book()
# sht = wb.sheets.add(sheet_name)
# wb.save(file)

# with xw.App() as app:
#     book = app.books[file]



# wb = xw.Book(file)
# wb.book.visible = True
# wb.book.fullscreen = True

wb.book.active
sht = wb.sheets["test"]
# sht.activate

sht["A10"].value = [[1], [2], [3], [4], [5]]
print(sht["A1:A5"].value)

wb.close()
wb.save()


# print(sht[20, 0].__dir__())
# sht[21:4, 22:4].value = "A"


# sht["A1"].value = 5
# sht["B1"].value = 10
# sht["C1"].value = "=SUM(A1:B1)"
# result = sht["C1"].value
# print(result, sht.cell(row=1, column=3).value)
# # if sht["C1"].cell_type == "formula":
# #     result_formula = sht["C1"].formula
# #     print(result_formula)



# # # sheet = book.sheets["template"].copy(name="report")
# # # df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
# # # sheet.render_template(df=df)



# df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
# sht["A1"].value = df
# sht["A1"].options(pd.DataFrame, expand="table").value

# sht["A1"].expand().font.name = "JetBrains Mono"

# sht.cells(5, 5).value = "test"
# sht.range("A3:A26").api.Font.Size = 25

# my_range = sht.range((5, 5), (9, 9))
# my_range.color = (255, 255, 255)
# my_range.value = 1


# sht.cells(10, 10).value = df

# sht.range("A15").color = None
# print(sht.range("A15").color is None)

# wb.save(file)