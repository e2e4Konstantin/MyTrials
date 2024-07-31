
# pip install pywin32
# import sys
# sys.path.append("C:\\_path_to_virtual_environment\\Lib\\site-packages\\")
# https://learn.microsoft.com/ru-ru/office/vba/api/word.wdviewtype
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word?view=word-pia
# https://github.com/luxiao/python/blob/master/aia/work/easyword.py
# http://www.icodeguru.com/webserver/Python-Programming-on-Win32/ch10.htm
import os
import win32com.client
from win32com.client import constants as win32consts
# from win32com import pythoncom
from pathlib import WindowsPath





# wdNormalView = constants.wdNormalView

file_path = os.path.abspath(os.path.join('.', 'word', 'limonad.docx'))

if not os.path.exists(file_path):
    print('File not found.')
    exit(1)




wdFormatPDF = 17

in_file = WindowsPath(r".\word\myfile.docx").resolve()
out_file = in_file.with_suffix(".pdf")
print(in_file)
print(out_file)


# word = win32com.client.Dispatch('Word.Application')
word = win32com.client.gencache.EnsureDispatch('Word.Application')

word.Visible = True
doc = word.Documents.Open(file_path, Visible=False)
# константы доступны только после создания объекта
# print(win32consts.__dir__()) # 
# print(win32consts.__dict__)
# print(win32consts.wdIndent)

# print(word.ListCommands(1))
print(doc.Tables.Count)

# for field in doc.Fields:
#     print(field)
inlineShapes = doc.InlineShapes
for shape in inlineShapes:
  print(shape.Type)
  if shape.Type in [
      win32consts.wdInlineShapeEmbeddedOLEObject, 
      win32consts.wdInlineShapeLinkedOLEObject, 
      win32consts.wdInlineShapeOLEControlObject]:
    print(True)
print(False)


doc.Top = 1
doc.Content.Text = "hello world"

doc.Content.Paragraphs.Add()
doc.Content.InsertAfter("hello2 ?")
doc.Content.InsertAfter("hello world 3")

location = doc.Range()
location.Move()
table = doc.Content.Tables.Add(location, 2, 4)
table2 = doc.Content.Tables.Add(location, 2, 2)

table2.PreferredWidth = 40

table.ApplyStyleHeadingRows = 0 
table.AutoFormat(16)
table.PreferredWidth = 400

doc.Content.InsertAfter("hello4 hello5")




# # word.ActiveDocument.ActiveWindow.View.Type = 3  
# # speaker = win32com.client.Dispatch("SAPI.SpVoice")
# # speaker.Speak("It works. Hoorah!")

# print(doc.Content.Text)

# doc.SaveAs(str(out_file), FileFormat=wdFormatPDF)
# par = doc.Content.Paragraphs.Add()
# par.Range.Text = 'Hello, world!'

# # Save and close document
# doc.Save()
# # doc.ActiveDocument.SaveAs(new_file)


doc.Close()
word.Quit()


# def OpenExcelSheet(filename):
#     try:
#         xl = Dispatch("Excel.Application")
#         xl.Workbooks.Open(filename)
#     except pythoncom.com_error, (hr, msg, exc, arg):
#         print "The Excel call failed with code %d: %s" % (hr, msg)
#         if exc is None:
#             print "There is no extended error information"
#         else:
#             wcode, source, text, helpFile, helpId, scode = exc
#             print "The source of the error is", source
#             print "The error message is", text
#             print "More info can be found in %s (id=%d)" % (helpFile, helpId)
