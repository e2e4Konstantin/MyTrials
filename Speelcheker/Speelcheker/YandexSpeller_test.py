import pandas as pd
import re
import pyaspeller
from spellchecker import SpellChecker
import enchant


parquet_file = 'template_all_output.gzip'

df = pd.read_parquet(parquet_file)
df['PARAMETER_BY_WORD'] = df['PARAMETER_TITLE'].str.lower().str.strip().str.split(' |;|,|:|/')
print(df.head(10), '\n', type(df), len(df))

unic_parameter_title = set(df['PARAMETER_TITLE'])
print(len(unic_parameter_title), unic_parameter_title)

# уникальные слова без цифр
unic_words = set([word for split_parameter in df['PARAMETER_BY_WORD'] for word in split_parameter if not word.isdigit()])
print(len(unic_words), unic_words)

# сокращения
separator = re.compile(r"[()\'\"\\/]")
abbreviation = set([word for word in unic_words if separator.match(word)])
print(abbreviation)

# убираем сокращения из уникальных слов
unic_words = list(set(unic_words).difference(abbreviation))
unic_words.sort()
print(len(unic_words), unic_words)

speller = pyaspeller.YandexSpeller(lang='ru', find_repeat_words=False)


for word in unic_words:
    for change in speller.spell(word):
        print(change)
print('<-------->')
# for word in unic_parameter_title:
#     for change in speller.spell(word):
#         print(word, change)
# print('<-------->')

# spell = SpellChecker(language='ru')
# print(f"ошибки: \n")
# for word in unic_words:
#     # print(word, spell.unknown(word))
#     if spell.correction(word) != word:
#         print(f"{word} --> {spell.correction(word)!r} или варианты: {spell.candidates(word)}")


d = enchant.Dict("ru_RU")
print(enchant.dict_exists("ru_RU"))
print(d)
print(d.tag)

for word in unic_words:
    if not d.check(word):
        print(word, d.check(word))



