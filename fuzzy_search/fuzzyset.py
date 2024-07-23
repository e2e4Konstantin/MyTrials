from fuzzyset import FuzzySet
corpus = """It was a murky and stormy night. I was all alone sitting on a crimson chair. I was not completely alone as I had three felines
    It was a murky and tempestuous night. I was all alone sitting on a crimson cathedra. I was not completely alone as I had three felines
    I was all alone sitting on a crimson cathedra. I was not completely alone as I had three felines. It was a murky and tempestuous night.
    It was a dark and stormy night. I was not alone. I was not sitting on a red chair. I had three cats."""
corpus = [line.lstrip() for line in corpus.split("\n")]
fs = FuzzySet(corpus)
query = "It was a dark and stormy night. I was all alone sitting on a red chair. I was not completely alone as I had three cats."
x = fs.get(query)
print(x)


text    = 'на 1 м2 общей площади квартир в доме'

target  = 'на 1 м2 общей площади квартир' # 
fs = FuzzySet(text.split())

print(fs.get(target))