import xlwings as xw 
file_name = r"C:\Users\kazak.ke\Documents\PythonProjects\MyTrials\xlwings\Book1.xlsx"

wb = xw.Book(file_name)

# ws = xw.Book(file_name).sheets['test'] 


wks = xw.sheets 
print("Страницы :\n", wks) 
ws = wks[0] 
  
val = ws.range("A1").value 
print("A value in sheet1 :", val) 


r = ws.range("4:4").value 
print("Row :", r) 
  
c = ws.range("C:C").value 
print("Column :", c) 
  

table = ws.range("A1:C4").value 
print("Table :", table)

automatic = ws.range("A1").expand().value 
print("Automatic Table :", automatic) 

ws.range("A1").value = "geeks"
  
# Writing multiple values 
# to a cell for automatic 
# data placement 
ws.range("B1").value = ["for", "geeks"] 
  
# Writing 2D data to a cell 
# to automatically put data 
# into correct cells 
ws.range("A2").value = [[1, 2, 3], ['a', 'b', 'c']] 
  
# Writing multiple data to 
# multiple cells 
ws.range("A4:C4").value = ["This", "is", "awesome"] 
  
# Outputting entire table 
print("Table :\n", ws.range("A1").expand().value) 