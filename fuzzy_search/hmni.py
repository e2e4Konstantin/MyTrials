# https://github.com/Christopher-Thornton/hmni
# pip install hmni
import hmni
matcher = hmni.Matcher(model='latin')
# hmni.Matcher(model='cyrillic')


r = matcher.similarity('Alan', 'Al')
print(r)
# 0.6838303319889133

r = matcher.similarity('Alan', 'Al', prob=False)
print(r)
# 1

r = matcher.similarity('Alan Turing', 'Al Turing', surname_first=False)
print(r)
# 0.6838303319889133