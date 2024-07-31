import win32com.client
word = win32com.client.gencache.EnsureDispatch('Word.Application')

NrLines = 10

doc=word.Documents.Add()

# rang = doc.Range(Start=0,End=0)
rang = doc.Range(Start=0, End=doc.Content.End - 1)
doc.Tables.Add(rang,NumRows=2,NumColumns=1)

index=2+NrLines
doc.Tables(1).Rows(2).Cells(1).Split(1,3)

width = doc.Tables(1).Rows(1).Cells(1).Width
doc.Tables(1).Rows(1).Cells(1).Range.Bold=True
doc.Tables(1).Rows(1).Cells(1).Range.Font.Size=15
doc.Tables(1).Rows(1).Cells(1).Range.Text='Report of LoadFlow Calculations from PowerFactory'
doc.Tables(1).Cell(2,1).Range.Text='Name of the line'
doc.Tables(1).Cell(2,2).Range.Text='Loading'
doc.Tables(1).Cell(2,3).Range.Text='Comment'

# word.PrintPlain(doc.Tables(1).Rows(2).Cells)

for i in range(NrLines):
    doc.Tables(1).Rows.Add()
    doc.Tables(1).Cell(i+3,1).Range.Text=i+5
    doc.Tables(1).Cell(i+3,2).Range.Text=i+33
    # 
    doc.Tables(1).Cell(i+3,3).Range.Font.Color=225
    doc.Tables(1).Cell(i+3,3).Range.Text='LoadingOver 60%'

doc.Save("myfile.docx")


doc.Close()
word.Quit()

def updateTable(name,tableCount):

    #tell word to open the document
    word.Documents.Open (IP_Directory_Dest + "\\" + name)

    #open it internally
    doc = word.Documents(1)

    # answer to Question # 2 (how to update a specific cell in a TABLE)
    # clearing Table # 1, Row # 1, cell # 1 content
    doc.Tables (1). Rows (1). Cells (1). Range.Text = ''

    #Clearing Table # 1, Row # 1, Col # 4 content to blank
    doc.Tables (1). Cell(1, 4). Range.Text = ''

    # specifically select TABLE # tableCount
    table = doc.Tables(tableCount)
    # count the number of rows in TABLE # 1
    numRows = table.Rows.Count

    # count number of columns
    numCols = table.Columns.Count

    print ('Number of Rows in TABLE',numRows)
    print ('Number of Columns in TABLE',numCols)


    # NOTE : ROW # 1 WILL NOT BE DELETED, AS IT IS COMMON FOR BOTH IP AND IR
    # delete and add the same number of rows
    for row in range(numRows):
        # add a row at the end of table
        doc.Tables(tableCount).Rows.Add ()
        # delete row 2 of table (so as to make the effect of adding rows equal)
        doc.Tables(tableCount).Rows(2).Delete()


doc.Tables(1).Rows(1).Delete()


 table = doc.Tables(1)
    # count the number of rows in TABLE # 1
    numRows = table.Rows.Count

    # count number of columns
    numCols = table.Columns.Count

    print ('Number of Rows in TABLE',numRows)
    print ('Number of Columns in TABLE',numCols)

    # print the row 1 of TABLE # 1 -- for checking
    print ('### 1 - CHECK this ONE ... ',table.Rows(1).Range.Text)

    # delete row 1 of table 1
    doc.Tables(1).Rows(1).Delete()
    # delete cell 1,1 of table 1
    doc.Tables(1).Cell(1, 1).Delete()

    # again count the number of rows in table
    numRows = table.Rows.Count

    print numRows

    # print the row 1 of TABLE # 1 -- after Deleting the first ROW --> for checking
    print ('### 2 - CHECK this ONE ... ',table.Rows(1).Range.Text)

    # get the number of tables
    numberTables = doc.Tables.Count
    # count the number of tables in document
    print numberTables

    #delete ALL tables
    tables = doc.Tables
    for table in tables:
        # to get  the content of Row # 1, Column # 1 of table
        print table.Cell(Row =1, Column = 1).Range.Text
##        table.Delete(Row =2)
        # this one deletes the whole table (which is not needed)
        #table.Delete()