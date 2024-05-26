excel = win32.gencache.EnsureDispatch('Excel.Application')
file_location = 'C:\Users\A42918\Desktop\Test_folder\Abild, T1.xls'
wb = excel.Workbooks.Open(file_location)

ws = wb.Worksheets("Trelindad_utan")
ws.Range('AH4').Interior.ColorIndex = 37
ws.Range('AH4').Font.Bold = True
comment = 'E14678: Vinkel i nollpunkt. Sätts lika med vinkeln på I-bus i balansnätet (om denna avviker mycket från noll grader).'.decode('utf-8')
# remove any previous comments just in case
ws.Range('AH4').ClearComments
# Add the comment, and its text:
cmt = ws.Range('AH4').AddComment(comment)
# Ensure the comment is not bolded font
cmt.Shape.TextFrame.Characters().Font.Bold = False

# -------------------------------------------------------------

excel = win32.gencache.EnsureDispatch('Excel.Application')
file_location = 'C:\Users\A42918\Desktop\Test_folder\Abild, T1.xls'
wb = excel.Workbooks.Open(file_location)

ws = wb.Worksheets("Trelindad_utan")
ws.Range('AH4').Interior.ColorIndex = 37
ws.Range('AH4').Font.Bold = True

ws.Range('AH4').ClearComments
comment = 'E14678: Vinkel i nollpunkt. Sätts lika med vinkeln på I-bus i balansnätet (om denna avviker mycket från noll grader).'.decode('utf-8')

cmt = ws.Range('AH4').AddComment(comment)

cmt.Shape.TextFrame.Characters().Font.Bold = False

wb.SaveAs(Filename = 'C:\Users\A42918\Desktop\color_resultat.xls')

excel.Application.Quit()
