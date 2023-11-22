# pip install -U textblob
# python -m textblob.download_corpora

# import polyglot
# from polyglot.text import Text, Word


from textblob import TextBlob

text = "Длинна реки, длина волос. Длинная дорога."

blob = TextBlob(text)
print(blob.tags)

print(blob.words)
print(blob.sentiment)


print(blob.words[1].singularize())
print(blob.words[1].pluralize())
print(blob.words[1].lemmatize())

print(blob.parse())
print(blob.ngrams(n=3))


print(blob.correct())
