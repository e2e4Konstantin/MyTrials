#
# pip install pyaspeller
#
# на количество обращений к Сервису - в размере 10 тысяч обращений в сутки;
# на объем проверяемого текста - в размере 10 миллионов символов в сутки.



import pyaspeller
speller = pyaspeller.YandexSpeller()

text = 'Кислое Малако. Длинная длинна. Река длиНа и широка. ПрАверкка текста на ашибки.'

fixed = speller.spelled(text)
print(fixed)

check = pyaspeller.Word('длинна')
print(check.correct)
print(check.variants)
print(check.spellsafe)

for change in speller.spell(text):
    print(change)