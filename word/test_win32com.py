
# pip install pywin32
# import sys
# sys.path.append("C:\\_path_to_virtual_environment\\Lib\\site-packages\\")
# https://learn.microsoft.com/ru-ru/office/vba/api/word.wdviewtype
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word?view=word-pia
import os
import win32com.client
from win32com.client import constants
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

word.Visible = False
doc = word.Documents.Open(file_path, Visible=False)
for field in doc.Fields:
    print(field)

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
