# pip install docx2python

from docx2python import docx2python
from docx2python.iterators import enum_cells

def remove_empty_paragraphs(tables):
    for (i, j, k), cell in enum_cells(tables):
        tables[i][j][k] = [x for x in cell if x]

def main():
    with docx2python('./word/Limonad.docx') as doc:
        print(doc.text)
        print(doc.body)
        print(type(doc.body))
        print(doc.comments)
        print(dir(doc))
        print(doc.tables)
        

if __name__ == "__main__":
    # doc = docx2python('./word/Limonad.docx')
    # print(doc.text)
    # doc_body = doc.body
    # print(doc_body)
    # table = doc_body[table_number]
    # table = pd.DataFrame(table)

    main()