import win32com.client

wordapp = win32com.client.Dispatch("Word.Application") 
wordapp.Visible = 1 
wd = wordapp.Documents.Add()
wd.PageSetup.Orientation = 1 
wd.PageSetup.BookFoldPrinting = 1 
wd.Content.Font.Size = 11
wd.Content.Paragraphs.TabStops.Add (100)
wd.Content.Text = "Hello, I am a text!"

location = wd.Range()
location.Paragraphs.Add()
location.Collapse(0)


location.Paragraphs.Add()
location.Collapse(1)
table = location.Tables.Add (location, 3, 4)
table.ApplyStyleHeadingRows = 1
table.AutoFormat(16)
table.Cell(1,1).Range.InsertAfter("Teacher")

location1 = wd.Range()
location1.Paragraphs.Add()
location1.Collapse(1)
table = location1.Tables.Add (location1, 3, 4)
table.ApplyStyleHeadingRows = 1
table.AutoFormat(16)
table.Cell(1,1).Range.InsertAfter("Teacher1")
wd.Content.MoveEnd
wd.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Application