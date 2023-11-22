from pydantic import BaseModel, Field

import re

_patters = {
    'quote': r"^\s*\d+\.\d+(-\d+){2}\s*$",  # 3.1-24-1 Расценка
    'table': r"^\s*\d+\.\d+(-\d+){4}\s*$",  # 3.1-1-5-0-24 Таблица
    'subsection': r"^\s*\d+\.\d+(-\d+){2}\s*$",  # 3.1-1-5 Раздел
    'section': r"^\s*\d+\.\d+(-\d+){1}\s*$",  # 7.9-1 Отдел
    'collection': r"^\s*\d+\.\d+\s*$",  # 7.9 Сборник
    'chapter': r"^\s*\d+\s*$",  # 7 Глава
}


class Quote(BaseModel):
    code: str = Field(pattern=_patters['quote'])  # 3.1-24-1
    title: str
    table: str = Field(pattern=_patters['table'])  # 3.1-1-5-0-24
    subsection: str | None = None
    section: str | None = None
    collection: str | None = None
    chapter: str | None = None


class Table(BaseModel):
    code: str = Field(pattern=_patters['table'])  # 9.1-1-1-0-2
    title: str
    subsection: str | None = Field(pattern=_patters['subsection'])  # 3.1-1-5
    section: str | None = None
    collection: str | None = None
    chapter: str | None = None


# 8.2-1-1 Раздел 1.1.1. Ультразвуковой контроль и механические испытания сварных соединений газопроводов
class Subsection(BaseModel):
    code: str = Field(pattern=_patters['subsection'])
    title: str
    section: str = Field(pattern=_patters['section'])
    collection: str | None = None
    chapter: str | None = None


# 8.2-1	Отдел 1.1. Контроль качества сварных соединений
class Section(BaseModel):
    code: str = Field(pattern=_patters['section'])
    title: str
    collection: str = Field(pattern=_patters['collection'])
    chapter: str | None = None


# 8.2 Сборник 2. Контроль качества соединений стальных и полиэтиленовых газопроводов
class Collection(BaseModel):
    code: str = Field(pattern=_patters['collection'])
    title: str
    chapter: str = Field(pattern=_patters['chapter'])


# 8	Глава 8. Нормы накладных расходов и сметной прибыли
class Chapter(BaseModel):
    code: str = Field(pattern=_patters['chapter'])
    title: str


class Catalog(BaseModel):
    quote: list[Quote] = []
    table: list[Table] = []
    subsection: list[Subsection] = []
    section: list[Section] = []
    collection: list[Collection] = []
    chapter: list[Chapter] = []


quote = Quote(code='3.1-24-1', title='Срезка недобора грунта в выемках группа грунтов 1-3', table='3.1-1-5-0-24')
table = Table(code='9.1-1-1-0-2', subsection='9.1-1-1',
              title='Временное отопление, законченных вчерне производственных зданий промышленных предприятий')
subsection = Subsection(code='8.2-1-1', section='8.2-1',
                        title='Ультразвуковой контроль и механические испытания сварных соединений газопроводов')
section = Section(code='8.2-1', collection='8.2', title='Контроль качества сварных соединений')
collection = Collection(code='8.2', chapter='8',
                        title='Контроль качества соединений стальных и полиэтиленовых газопроводов')
chapter = Chapter(code='8', title='Нормы накладных расходов и сметной прибыли')

print(f" {quote=}\n {table=}\n {subsection=}\n {section=}\n {collection=}\n {chapter=}")

