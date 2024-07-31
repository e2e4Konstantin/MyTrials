import aspose.words as aw

# Load the document from the disc.
doc = aw.Document("./word/Limonad.docx")

# Save the document to HTML format.
doc.save("./word/Limonad.html")
doc.save("./word/Limonad.pdf")