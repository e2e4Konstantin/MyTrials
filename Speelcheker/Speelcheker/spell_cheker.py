from difflib import SequenceMatcher, get_close_matches
import pandas as pd
import os
from spellchecker import SpellChecker
from pprint import pprint


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

options_synonym: dict[str: list[str]] = {
    'высота': ['выста', 'высата'],
    'глубина': ['глубна', 'глубин'],
    'грузоподъемность': ['грузоподъёмность', 'грузаподъемность', 'грузподъемность', 'грузоподъемность', 'грузоподемность', 'грузоподьемность'],
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


options_dubious: dict[str: list[str]] = {
    'условное': {'synonym': ['условный', 'условный'], 'replacement': 'Давление условное', 'help': 'значимое слово поставить первым'},
    'номинальный': {'synonym': ['номинальное', 'номинальная'], 'replacement': 'диаметр труб номинальный', 'help': 'значимое слово поставить первым'},
    'вместимость': {'synonym': ['вместительность'], 'replacement': 'может объем?', 'help': 'вместительность трудно измерить.'},
    'наружный': {'synonym': [], 'replacement': 'диаметр труб Наружный', 'help': 'значимое слово поставить первым'},
    'номер': {'synonym': ['номера', 'номеров'], 'replacement': '????', 'help': 'в чем измерить номер?'},
    'относ': {'synonym': [], 'replacement': '???', 'help': 'что такое относ?'},
    'марка': {'synonym': [], 'replacement': '???', 'help': 'в чем измеряется марка?'},
}



# path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\production\Quotes_Parsing\output"
# file_name = r"template_all_output.xlsx"
# file_name = os.path.join(path, file_name)
# sheet_name = "Options"
parquet_file = 'template_all_output.gzip'

# df = pd.read_excel(io=file_name, sheet_name=sheet_name, dtype=pd.StringDtype())
# columns = ['PRESSMARK', 'PARAMETER_TITLE']
# df = df[columns]
# df.to_parquet(parquet_file, compression='gzip')


df = pd.read_parquet(parquet_file)
df['PARAMETER_FIRST_WORD'] = df['PARAMETER_TITLE'].str.split(' |;|,|:|/').str.get(0).str.lower().str.strip()
df['PARAMETER_BY_WORD'] = df['PARAMETER_TITLE'].str.lower().str.strip().str.split(' |;|,|:|/')
print(df.head(10), '\n', type(df), len(df))

# for x in df.to_records(index=False):
#     print(x)

parameter_first_word = set(df['PARAMETER_FIRST_WORD'])
print(len(parameter_first_word), parameter_first_word)

misspelled = tuple([x for x in parameter_first_word if x not in options_synonym])
print(len(misspelled), misspelled)

keys = list(options_dubious.keys())
for x in list(options_dubious.keys()):
    keys.extend(options_dubious[x]['synonym'])
print(keys)

orfo = []
for word in misspelled:

    variants = get_close_matches(word, keys)
    if len(variants) < 1:
        orfo.append(word)
    else:
        print(word, ' -> ', variants)



spell = SpellChecker(language='ru')
print(f"ошибки: {orfo}\n")
for word in orfo:
    print(f"{word!r} --> {spell.candidates(word)} ")
    # print(word,  ' --> ',  spell.correction(word), '. или варианты:  ', spell.candidates(word))

