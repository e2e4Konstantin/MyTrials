import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint


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
df = df.convert_dtypes()
# print(df.dtypes)


# .filter(['B', 'C', 'D', 'E', 'F', 'G', 'H'])
# .filter(['G', 'H'])
# .str.contains('Сборник', case=False).head(20)
# print(df.loc[:, ['G', 'H'] ])
# .notna()


# print(df[df['H'].notna()].H.str.contains('Сборник', case=False))
# h = df[df['H'].notna()].H.str.contains('Сборник', case=False)

# h = df[df[df.H.notna()].H.str.contains('Сборник', case=False)]

#
# h1 = df[df['H'].notna()].filter(['C', 'H'])  # .H.str.strip().str.lower()
# print(h1.columns)
# print(h1)
# h1['H'] = h1['H'].str.strip().str.lower()
# print(h1)

# value = h1.iat[3, 1]
# print(f" *{value}* ")
#
# # print(h1[h1['H'].str.contains('Сборник', case=False)].filter(['B', 'C', 'D', 'E', 'F', 'G', 'H']) )
#
# #
# exp = r"^\s*Сборник\s+\d+\."
# collect = h1[h1['H'].str.contains(exp, case=False, regex=True)].filter(['C', 'H'])
#
# print(collect.info(verbose=False, memory_usage=True, show_counts=True))
# print(collect.shape)
# print(collect.index)
# print(collect)
# collect['H'] = collect['H'].str.strip().str.lower()  # .str.split(" ", n=2, expand=True)
# # print(collect)
#
# # #
# # #
# table_collection = []
# for row in range(0, collect.shape[0]):
#     value = collect.at[collect.index[row], 'H'].split()
#     table_collection.append((collect.index[row], value[1][:-1], " ".join(value[2:]).capitalize()))
#     print(row, collect.index[row], table_collection[-1:])
#
# pprint(table_collection, width=200)

#
#
# column_index = data.df.columns.get_loc(column_name)
#     data.column_names.index(column_name)
#     print(f"непустых значений в столбце {column_name!r}: {data.df[data.df.columns[column_index]].count()}")

# ---------------------------------------------------------------



cols = df[df['H'].notna()].filter(['B', 'C', 'D', 'E', 'F', 'H'])
print(cols.dtypes)
print(cols)
exp = r"^\s*Отдел\s+\d+\."
cols = cols[cols['H'].str.contains(exp, case=False, regex=True)]
print(cols)




def get_section_data(row: int, data_frame: DataFrame) -> tuple[int, str, str, str, str]:
    """ Получает данные об Отделе из data_frame на строке row. """
    index = data_frame.index[row]                               # индекс совпадает с номером строки в в файле
    chapter_cod = data_frame.at[index, 'B'].strip()             # глава
    collection_cod = data_frame.at[index, 'C'].strip()          # сборник
    section_field = data_frame.at[index, 'H'].split()
    section_number = section_field[1][:-1]                      # номер отдела
    section_title = " ".join(section_field[2:]).capitalize()    # название отдела
    return index, chapter_cod, collection_cod, section_number, section_title


sections = [get_section_data(row, cols) for row in range(cols.shape[0])]
pprint(sections, width=300)

#
# def get_sub_section_data(row: int, data_frame: DataFrame) -> tuple[int, str, str, str]:
#     """ Получает данные об Разделе из data_frame на строке row. """
#     index = data_frame.index[row]                               # индекс совпадает с номером строки в в файле
#     chapter_cod = data_frame.at[index, 'B'].strip()             # глава
#     collection_cod = data_frame.at[index, 'C'].strip()          # сборник
#
#     section_title = data_frame.at[index, 'H'].split()
#     return index, chapter, collection_cod, section_title[1][:-1], " ".join(section_title[2:]).capitalize()


