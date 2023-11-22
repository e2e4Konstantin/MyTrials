#
import pyaspeller
speller = pyaspeller.YandexSpeller()

text = 'Длинна реки, длинна волос. Длиная дорога. Малоко белое.'

fixed = speller.spelled(text)
print(fixed)

check = pyaspeller.Word('длинна')
print(check.correct)
print(check.variants)
print(check.spellsafe)

for change in speller.spell(text):
    print(change)