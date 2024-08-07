# https://pythonexcels.com/python/2009/10/05/python-excel-mini-cookbook
# https://github.com/trenton3983/Excel_Automation_with_Python

import win32com.client as win32
from pathlib import Path
import sys

win32c = win32.constants

def run_excel(file_name: str) -> list:

    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True  # False
    try:
        wb = excel.Workbooks.Open(file_name)
    except Exception as e:
        print(f'{e}\n{file_name}')
        sys.exit(1)
    sheet_names = [sheet.Name for sheet in wb.Sheets]
    excel.DisplayAlerts = False
    wb.DisplayAlerts = False
    wb.SaveAs(r"2_test_save_as.xlsx", FileFormat=win32c.xlOpenXMLWorkbook) # xlWorkbookDefault

    wb.Close(True)
    excel.Quit()
    return sheet_names


f_name = r"C:\Users\kazak.ke\Documents\Дамир\21.1-2-1+.xls"


sheets = run_excel(f_name)
print(sheets)
