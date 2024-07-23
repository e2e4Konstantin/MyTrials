from thefuzz import fuzz
name = "Kurtis Pykes"
full_name = "Kurtis K D Pykes"

print(f"Similarity score: {fuzz.ratio(name, full_name)}")
print(f"Similarity score: {fuzz.partial_ratio(name, full_name)}")
print()
# text    = 'на 1 м2 общей площади квартир в доме'
# text    = 'на 1 м2 общей площади квартир'
text    = ' площади квaртир на 1 м2 общей'
target  = 'на 1 м2 общей площади квартир' 
print(f"{fuzz.ratio(target, text) = }")
print(f"{fuzz.partial_ratio(target, text) = }")
print(f"{fuzz.token_sort_ratio(target, text) = }")
print(f"{fuzz.token_sort_ratio(target, text) = }")

