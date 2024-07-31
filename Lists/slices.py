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

l2 = [1, 23.5, 77, 56 ]

print(l2[0:])  
print(f"без первого: {l2[1:]}")
print(l2[:1])  
print(f"последний: {l2[-1]}")
print(f"последний 2: {l2[-2:]}")
s = "привет\nпока\n\n"
print(s, "--")
print(f"{s[:-2]!r}")