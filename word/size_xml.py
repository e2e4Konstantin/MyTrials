# https://www.youtube.com/shorts/1Mgb95yigkk
import docx
from docx.oxml.table import CT_Row, CT_Tc
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx import Document

doc = docx.Document('example.docx')

# all  tables via XML
for table in doc.tables:
    table.style = 'Normal Table'
    tbl = table._tbl  # get xml element in table
    tblPr = tbl.tblPr  # We get an xml element containing the style and width

    print('============================ before  ==============================')
    print(table._tbl.xml)  # Output the entire xml of the table
    # Setting the table width to 100%. To do this, look at the xml example:
    # <w:tblW w:w="5000" w:type="pct"/> - this is size 5000 = 100%, and type pct = %
    #
    tblW = OxmlElement('w:tblW')
    w = OxmlElement('w:w')
    w.set(qn('w:w'), '5000')
    type = OxmlElement('w:type')
    type.set(qn('w:type'), 'pct')
    w.set(qn('w:type'), 'pct')
    

    print('============================ after ==============================')
    print(table._tbl.xml)  # Output the entire xml of the table

doc.save('restyled.docx')