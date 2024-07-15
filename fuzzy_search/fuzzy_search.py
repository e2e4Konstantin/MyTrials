from fuzzywuzzy import process
from fuzzywuzzy import fuzz

str_list = ['Joe Biden', 'Joseph Biden', 'Joseph R Biden']

match_ratios = process.extract('joe r biden', str_list, scorer=fuzz.token_sort_ratio)
print(match_ratios)

best_match = process.extractOne('joe r biden', str_list, scorer=fuzz.token_sort_ratio)
print(best_match)


str1 = 'Chocolate Strawberry Cake'
str2 = 'Strawberry Chocolate Cake'

token_set_ratio = fuzz.token_set_ratio(str1, str2)
print(token_set_ratio)