import re
from difflib import SequenceMatcher, get_close_matches
import pandas as pd
import os
from spellchecker import SpellChecker
from pprint import pprint

options_synonym: dict[str: list[str]] = {
    'высота': ['выста', 'высата'],
    'глубина': ['глубна', 'глубин'],
    'грузоподъемность': ['грузоподъёмность', 'грузаподъемность', 'грузподъемность', 'грузоподемность',
                         'грузоподьемность'],
    'давление': ['довление'], 'диагональ': ['диаганаль'],
    'диаметр': ['диаметер'],
    'длина': ['длинна', 'длна'],
    'количество': ['количеством', 'колличество'],
    'масса': [],
    'мощность': ['мощьность', 'мошность'],
    'нагрузка': [],
    'напряжение': [],
    'объем': [],
    'отверстие': [],
    'паропроизводительность': [],
    'перемещение': [],
    'периметр': [],
    'плотность': [],
    'площадь': [],
    'предел': [],
    'продолжительность': [],
    'производительность': [],
    'прочность': [],
    'радиус': [],
    'расстояние': ['растояние'],
    'расход': [],
    'сечение': [],
    'скорость': [],
    'сторона': ['старана'],
    'температура': ['темпратура', 'темпиратура'],
    'теплопроизводительность': ['теплпроизводительность'],
    'ток': ['так'],
    'толщина': ['талщина'],
    'усилие': [],
    'холодоотдача': [],
    'холодопроизводительность': [],
    'частота': ['чистота'],
    'шаг': ['шагов'],
    'ширина': ['шырина']}


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


#
parquet_file = 'template_all_output.gzip'

df = pd.read_parquet(parquet_file)
# df['PARAMETER_FIRST_WORD'] = df['PARAMETER_TITLE'].str.split(' |;|,|:|/').str.get(0).str.lower().str.strip()
df['PARAMETER_BY_WORD'] = df['PARAMETER_TITLE'].str.lower().str.strip().str.split(' |;|,|:|/')
print(df.head(5), '\n', type(df), len(df))

spell = SpellChecker(language='ru')

l = [w for x in df['PARAMETER_BY_WORD'] for w in x]

# l = [w for x in df['PARAMETER_BY_WORD'] for w in x if w not in options_synonym.keys()]
ls = set(l)
print(len(ls), ls)

ln = [w for w in list(ls) if w not in options_synonym.keys() and not w.isdigit()]
ln.sort()
print(len(ln), ln)

# сокращения
separator = re.compile(r"[()\'\"\\/]")
abbreviation = set([w for w in ln if separator.match(w)])
print(abbreviation)
lnm = set(ln).difference(abbreviation)
print(len(lnm), lnm)
mistakes = spell.unknown(lnm)
print(len(mistakes), mistakes)
for mistake in mistakes:
    print(f'Ошибка: "{mistake}" --> Правильно: {spell.correction(mistake)}')




#
# lnm = [w for w in ln if spell.candidates(w) and w not in spell.candidates(w)]
# print(len(lnm), lnm)


#
# for w in ln:
#     print(f"{w} -> {spell.candidates(w)}") # {spell.candidates(w)} {spell.correction(w)}

# s = SequenceMatcher()
# w1 = 'высота'
# w2 = options_synonym['высота'][0]
# s.set_seqs(w1, w2)
# print(f"{w1} : {w2} ->  {s.ratio()}")
#
# w2 = options_synonym['высота'][1]
# s.set_seqs(w1, w2)
#
# print(f"{w1} : {w2} ->  {s.ratio()}")


# for x in options_synonym.keys():
#     for y in options_synonym[x]:
#         # s.set_seqs(x, y)
#         print(f"{x} : {y} ->  {SequenceMatcher(None, x, y).ratio():.4f} | {spell.candidates(y)}")
