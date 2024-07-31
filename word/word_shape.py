import win32com.client
import time

wapp = win32com.client.Dispatch("Word.Application") 
wapp.Visible = 1 
doc = wapp.Documents.Add()
color_index = 6
shape = doc.Shapes.AddShape(2, 10, 10, 100, 100)
shape.Fill.ForeColor.ObjectThemeColor = color_index
while True:
    color_index = (color_index + 1) % 16
    shape.Fill.ForeColor.ObjectThemeColor = color_index
    time.sleep(0.5)

doc.Close() # Close the Word Document (a save-Dialog pops up)
# wapp.Quit() # Close the Word Application