import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint
import gc
import re


# column_positions = {'глава': ['B', r"^\s*Глава\s+\d+\."],
#                     'сборник': ['C', r"^\s*Сборник\s+\d+\."],
#                     'отдел': ['D', r"^\s*Отдел\s+\d+\."],
#                     'раздел': ['E', r"^\s*Раздел\s+\d+\."],
#                     'таблица': ['F', r"^\s*Таблица\s+\d+\."],  # Таблица 3.1-1.
#                     'заголовок': ['H', r""]
#                     }
STRONG_MATCH = True
SOFT_MATCH = False

pattern_common_def = {
    "D": (re.compile(r"\d+\.\d+(-\d+){1}"), STRONG_MATCH),  # 3.6-1
    "E": (re.compile(r"\d+\.\d+(-\d+){2}"), STRONG_MATCH),  # 3.6-1-1
    "F": (re.compile(r"\d+\.\d+(-\d+){4}"), STRONG_MATCH),  # 3.6-1-1-0-1
}

pattern_quote = {}
pattern_quote.update(pattern_common_bc)
pattern_quote.update(pattern_common_def)
pattern_quote.update({"G": (re.compile(r"\d+\.\d+(-\d+)+"), STRONG_MATCH)})  # номер расценки '3.1-1-5'


column_positions = {
                    'глава': {
                        'column_title': 'B',
                        'cod_pattern': (re.compile(r"^\s*\d+\s*$"), STRONG_MATCH),              # 3
                        'title_pattern': (re.compile(r"^\s*Глава\s+\d+\."), SOFT_MATCH)
                    },
                    'сборник': {
                        'column_title': 'C',
                        'cod_pattern': (re.compile(r"^\s*\d+\.\d+\s*$"), STRONG_MATCH),         # 3.1
                        'title_pattern': (re.compile(r"^\s*Сборник\s+\d+\."), SOFT_MATCH)       # Сборник  3. Буровзрывные работы
                    },
                    'отдел': {
                        'column_title': 'D',
                        'cod_pattern': (re.compile(r"^\s*\d+\.\d+(-\d+){1}\s*$"), STRONG_MATCH),    # 3.1-2 / 3.1 ошибка в файле
                        'title_pattern': (re.compile(r"^\s*Отдел\s+\d+\."), SOFT_MATCH)        # Отдел  1. Свайные работы
                    },
                    'раздел': {
                        'column_title': 'E',
                        'cod_pattern': (re.compile(r"^\s*\d+\.\d+(-\d+){2}\s*$"), STRONG_MATCH),       # 3.1-1-5
                        'title_pattern': (re.compile(r"^\s*Раздел\s+\d+\."), SOFT_MATCH)            # Раздел  3. Разработка грунта скреперами
                    },
                    'таблица': {
                        'column_title':     'F',
                        'cod_pattern':      (re.compile(r"^\s*\d+\.\d+(-\d+){4}\s*$"), STRONG_MATCH),       # 3.1-1-1-0-2
                        'title_pattern':    (re.compile(r"^\s*Таблица\s+\d+\.\d+-\d+\."), SOFT_MATCH)       # Таблица 3.1-10. Разработка грунта скреперами самоходными
                    },
                    'расценка': {
                        'column_title':     'G',
                        'cod_pattern':      (re.compile(r"^\s*\d+\.\d+(-\d+){2}\s*$"), STRONG_MATCH),                 # 3.1-24-1
                        'title_pattern':    (re.compile(r""), SOFT_MATCH)                                   # свободный текст
                    },

                    'заголовок': {'column_title': 'H', 'cod_pattern': r"", 'title_pattern': r""}
                    }


def generate_column_names(length: int) -> list[str] | None:
    """ Создает список названий столбцов таблиц excel """
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    extra = []
    if 0 < length < 676:
        if length > len(alphabet):
            extra.extend(alphabet)
            for letter in alphabet:
                for letter_next in alphabet:
                    extra.append(f"{letter}{letter_next}")
                    if len(extra) >= length:
                        break
                if len(extra) >= length:
                    break
        return extra[:length]
    return None


def get_collection_data(row: int, data_frame: DataFrame) -> tuple[int, str, str, str, str]:
    """ Получает данные об Сборнике из data_frame на строке row. """
    index = data_frame.index[row]  # индекс совпадает с номером строки в файле
    chapter_cod = data_frame.at[index, 'B'].strip()  # код главы
    collection_cod = str(data_frame.at[index, 'C']).strip()  # код сборника
    collection_field = data_frame.at[index, 'H'].split()  # поле целиком
    collection_number = collection_field[1][:-1]  # номер сборника из заголовка
    collection_title = " ".join(collection_field[2:]).capitalize()  # название сборника
    return index, chapter_cod, collection_cod, collection_number, collection_title


def get_section_data(row: int, data_frame: DataFrame) -> tuple[int, str, str, str, str, str]:
    """ Получает данные об Отделе из data_frame на строке row. """
    index = data_frame.index[row]  # индекс совпадает с номером строки в файле
    chapter_cod = data_frame.at[index, 'B'].strip()  # код главы
    collection_cod = data_frame.at[index, 'C'].strip()  # код сборника
    section_cod = data_frame.at[index, 'D'].strip()  # код отдела
    section_field = data_frame.at[index, 'H'].split()
    section_number = section_field[1][:-1]  # номер отдела из заголовка
    section_title = " ".join(section_field[2:]).capitalize()  # название отдела
    return index, chapter_cod, collection_cod, f"{section_cod}-{section_number}", section_number, section_title


def get_subsection_data(row: int, data_frame: DataFrame) -> tuple[int, str, str, str, str, str, str]:
    """ Получает данные об Раздела из data_frame на строке row. """
    index = data_frame.index[row]  # индекс совпадает с номером строки в файле
    chapter_cod = data_frame.at[index, 'B'].strip()  # код главы
    collection_cod = data_frame.at[index, 'C'].strip()  # код сборника
    section_cod = data_frame.at[index, 'D'].strip()  # код отдела
    subsection_cod = data_frame.at[index, 'E'].strip()  # код раздела
    subsection_field = data_frame.at[index, 'H'].split()
    subsection_number = subsection_field[1][:-1]  # номер отдела из заголовка
    subsection_title = " ".join(subsection_field[2:]).capitalize()  # название отдела
    return index, chapter_cod, collection_cod, section_cod, subsection_cod, subsection_number, subsection_title


full_name = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\1_targets\tasck_2\sources\template_3_68.xlsx"
sheet_name = "name"
df = pd.read_excel(io=full_name, sheet_name=sheet_name, header=None, dtype="object")  # , nrows = 8300
print(df.info(verbose=False, memory_usage=True, show_counts=True))
print(df.shape)
# print(df.index)
# print(df.columns)
# print(df.dtypes)
column_names = generate_column_names(df.shape[1])
df.columns = column_names
# df = df.convert_dtypes()
# print(df.dtypes)
# ---------------------------------------------------------------

df_cut = df[df['H'].notna()].filter(['B', 'C', 'D', 'E', 'F', 'H'])
df_cut = df_cut.convert_dtypes()
print(df_cut.dtypes)
# print(df_cut)

column_name = column_positions['заголовок'][0]

collections_quote = df_cut[df_cut[column_name].str.contains(column_positions['сборник'][1], case=False, regex=True)]
# print(collections_quote)
collections = [get_collection_data(row, collections_quote) for row in range(collections_quote.shape[0])]
print('Сборники:', len(collections))
# pprint(collections, width=300)
del collections_quote
gc.collect()

sections_data = df_cut[df_cut[column_name].str.contains(column_positions['отдел'][1], case=False, regex=True)]
# print(sections_data)
sections = [get_section_data(row, sections_data) for row in range(sections_data.shape[0])]
print('Отделы:', len(sections))
# pprint(sections, width=300)
del sections_data
gc.collect()

subsections_data = df_cut[df_cut[column_name].str.contains(column_positions['раздел'][1], case=False, regex=True)]
subsections = [get_subsection_data(row, subsections_data) for row in range(subsections_data.shape[0])]
print('Разделы:', len(subsections))
# pprint(subsections, width=300)
del subsections_data
gc.collect()
