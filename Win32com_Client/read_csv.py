import win32com.client

excel_app = win32com.client.Dispatch('Excel.Application')
excel_app.Visible = True
excel_workbook = excel_app.Workbooks.Add()
# excel_workbook.Name = 'report_2020.01.01_23.10.xlsx'
excel_worksheet = excel_workbook.Worksheets.Add()
excel_worksheet.Name = 'sheet title'
# excel_workbook.Save()
excel_workbook.SaveAs('report_2020.01.01_23.10.xlsx')
excel_workbook.Close()
excel_app.Quit()
