# pip install pyenchant
# https://pypi.org/project/pyenchant/
# https://pyenchant.github.io/pyenchant/install.html

# нужны словари
# https://github.com/ONLYOFFICE/dictionaries/blob/master/ru_RU/ru_RU.dic
#


import enchant
import difflib

broker = enchant.Broker()
print(enchant.get_enchant_version())
print(broker.describe())
print(broker.list_languages())

d = enchant.Dict("ru_RU")
print(enchant.dict_exists("ru_RU"))
print(d)
# d = enchant.request_dict("ru_RU")
print(d)
print(d.tag)

text = "Длинна реки, длина волос. Длинная дорога. Малоко белое."

print(u"привт", d.check(u"привт"))
print("малоко", d.check("малоко"))
print("длинна", d.check("длинна"))  # длина': ['длинна', 'длна'],
print(d.check(text))

# неправильное написание
print(d.suggest("длина"))

from enchant.checker import SpellChecker

chkr = SpellChecker("ru_RU")
chkr.set_text(text)

print(chkr.lang)
for err in chkr:
    print(err)
    print("ERROR:", err.word)

print([i.word for i in chkr])

dif, max = {}, 0

w = "длина"
a = set(d.suggest(w))
print(a)
for x in a:
    tmp = difflib.SequenceMatcher(None, w, x).ratio()
    if tmp > 0.75:
        dif[x] = tmp
    if tmp > max:
        max = tmp

    print(tmp)
print(dif)
print(max)
