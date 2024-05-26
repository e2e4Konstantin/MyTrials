# https://github.com/trenton3983/Excel_Automation_with_Python

import win32com.client as win32
from pathlib import Path
import sys

win32c = win32.constants

def run_excel(f_path: Path, f_name: str) -> list:

    filename = f_path / f_name

    # create excel object
    excel = win32.gencache.EnsureDispatch('Excel.Application')

    # excel can be visible or not
    excel.Visible = True  # False

    # try except for file / path
    try:
        wb = excel.Workbooks.Open(filename)
    except com_error as e:
        if e.excepinfo[5] == -2146827284:
            print(f'Failed to open spreadsheet.  Invalid filename or location: {filename}')
        else:
            raise e
        sys.exit(1)

    # get worksheet names
    sheet_names = [sheet.Name for sheet in wb.Sheets]

    wb.Close(True)
    excel.Quit()

    return sheet_names

# ws = {f'ws{i}': wb.Sheets(sheet.Name) for i, sheet in enumerate(wb.Sheets)}
# ws['ws0'].Range('A1').Value = 1
# # file path
# f_path = Path.cwd()  # file in current working directory
# # f_path = Path(r'c:\...\Documents')  # file located somewhere else

# # excel file
# f_name = 'test.xlsx'

# # function call
# run_excel(f_path, f_name)

# # output
# ['Sheet1', 'Sheet2', 'Sheet3', 'Sheet4']

# # create a worksheet object
# ws1 = wb.Sheets('Sheet1')
