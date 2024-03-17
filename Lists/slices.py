numbs: list[int] = list(range(1, 11))
text: str = "Hello world!"

print(numbs, numbs[::-1])
print(text, text[::-1])

rev: slice = slice(None, None, -1)
f_five: slice = slice(None, 5)

print(numbs[rev], numbs[f_five])
print(text[rev], text[f_five])


l = ['#'] * 10
print(l)
