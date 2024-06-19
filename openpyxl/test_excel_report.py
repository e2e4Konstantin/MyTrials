
# from models import ExcelBase  # ExcelReport,
# with ExcelBase(report_file) as file:
#     print(file.workbook)
#     # print(file.workbook.sheetnames)
#     print(file.worksheet)
    # sheet = file.get_sheet(sheet_name, 0)
#     # print(sheet)

# import openpyxl


# report_file = "april_test.xlsx"
# sheet_name = "test"

# # try:
# #     workbook = openpyxl.load_workbook(report_file)
# #     # worksheet = workbook[sheet_name] if sheet_name else workbook.active
# # except FileNotFoundError:
# wb = openpyxl.Workbook()
# wb.save(report_file)

# print(workbook)
# print(workbook.sheetnames)
# # ws = workbook.worksheets[0]
# # print(ws)
# ws = workbook.create_sheet(sheet_name, 0)
# # ws = workbook.active
# ws.cell(1,1).value = "test"
# print(ws)
# workbook.save(report_file)
# workbook.close()

# from openpyxl import Workbook
# from openpyxl.worksheet.table import Table, TableStyleInfo

# xl_file_name = "new_test.xlsx"
# wb = Workbook()
# ws = wb.worksheets[0]
# ws.title = "aa_Table_Sheet"
# headers = ["header1", "header2", "header3"]
# for col in range(1, len(headers) + 1):
#     for row in range(1, 5):
#         if row == 1:
#             ws.cell(row, col).value = headers[col - 1]
#         else:
#             ws.cell(row, col).value = str(row)

# tbl = Table(displayName="t_Tbl_1", ref="A1:C4")
# style = TableStyleInfo(
#     name="TableStyleMedium9",
#     showFirstColumn=False,
#     showLastColumn=False,
#     showRowStripes=True,
#     showColumnStripes=True,
# )
# tbl.tableStyleInfo = style
# ws.add_table(tbl)
# wb.save("new_test.xlsx")


import openpyxl

workbook = openpyxl.load_workbook(Source_Path)

##your code appending and deleting values - which  I think sometimes causes the errors

workbook.save(Destination_Path)
workbook.close

# Now open it again
workbook = openpyxl.load_workbook(Destination_Path)

# Your Code to format

workbook.save(Destination_Path)
workbook.close