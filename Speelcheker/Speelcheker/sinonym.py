from difflib import SequenceMatcher, get_close_matches
import pandas as pd
from spellchecker import SpellChecker
from pprint import pprint



fp = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\production\Quotes_Parsing\src\options.xlsx"

# df = pd.read_csv(fp, delimiter=';', header=None, encoding='cp1251', dtype=pd.StringDtype())
# df = pd.read_excel(fp, header=None,  dtype=pd.StringDtype())
# # print(df.head(10))


options_synonym: dict[str: list[str]] = {
    'высота': ['выста', 'высата'], 'глубина': ['глубна', 'глубин'],
    'грузоподъёмность': ['грузаподъемность', 'грузподъемность', 'грузоподъемность', 'грузоподемность', 'грузоподьемность'],
    'давление': ['довление'], 'диагональ': ['диаганаль'], 'диаметр': ['диаметер'], 'длина': ['длинна', 'длна'],
    'количество': ['количеством', 'колличество'], 'марка': [], 'масса': [], 'мощность': ['мощьность'], 'нагрузка': [],
    'напряжение': [], 'наружный': [], 'номер': [], 'номинальное': ['номинальный'], 'объем': [], 'отверстие': [],
    'относ': [], 'паропроизводительность': [], 'перемещение': [], 'периметр': [], 'плотность': [], 'площадь': [],
    'предел': [], 'продолжительность': [], 'производительность': [], 'прочность': [], 'радиус': [],
    'расстояние': ['растояние'], 'расход': [], 'сечение': [], 'скорость': [],
    'сторона': ['старана'], 'температура': [], 'теплопроизводительность': ['теплпроизводительность'],
    'ток': ['так'], 'толщина': ['талщина'], 'усилие': [], 'условное': [], 'холодоотдача': [],
    'холодопроизводительность': [], 'частота': ['чистота'], 'шаг': ['шагов'], 'ширина': ['шырина']}

# for x in df.to_records(index=False):
#     options_synonym[x[0].lower()] = [y.lower() for y in list(x)[1:] if not pd.isna(y)]


# pprint(options_synonym)
# print(options_synonym)

spell = SpellChecker(language='ru')
#
# l = ['Высота', 'Выста', 'Высата']
#
# # misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])
# # misspelled = spell.unknown(['молоко', 'молако', 'карова', 'длина'])
# misspelled = spell.unknown(l)
#
# for word in misspelled:
#     print(word,  ' --> ',  spell.correction(word), '. или варианты:  ', spell.candidates(word))
#
#
# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()
#
# for k, v in options_synonym.items():
#     if len(v)>0:
#         for x in v:
#             print(k, x, similar(k, x), spell.unknown([x]), spell.candidates(x))

words = ['hello', 'Hallo', 'hi', 'house', 'key', 'screen', 'hallo', 'question', 'format']
n = 5
cutoff = 0.5
print(get_close_matches('hello', words, n, cutoff))

s = SequenceMatcher()
s.set_seqs("abcd", "bcde")
print(s.ratio())

s.set_seqs('высота', 'выста')
print(s.ratio())

s.set_seqs('высота', 'высата')
print(s.ratio())
