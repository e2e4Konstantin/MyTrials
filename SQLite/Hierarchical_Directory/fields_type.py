# https://rdbms.narod.ru/article/enum/index.html
# можноеще дополнительно хранить ID | ParentID | TopID для быстрого доступа к корневой записи
# https://stackoverflow.com/questions/5299267/how-to-create-enum-type-in-sqlite

import sqlite3
import os


print(sqlite3.version)
print(sqlite3.sqlite_version)

db_name = os.path.join(os.path.dirname(__file__), "h_dir.sqlite3")
# удаляем файл
if os.path.isfile(db_name):
    os.unlink(db_name)


# create table [Enumerations]
# (
#     [Id] int not null identity primary key,
#     [Parent] int references [Enumerations]([Id]),
#     [Code] varchar(120) not null unique,
#     [Name] varchar(120) not null
# )

# Enumerations
# Id	Parent	Code        	Name
#______________________________________________________________
# 1	    null	Enumerations	Справочник возможных значений
# 2	    1	    Employees   	Значения, касающиеся работников
# 3	    2	    SalaryTypes 	Виды оплаты труда
# 4	    3	    Piece	        Сдельная
# 5	    3	    Tariff	        Почасовая
# 6	    3	    Salary	        Оклад


query = """
    CREATE TABLE tbEnumeration (
    id_tblDirectory INTEGER PRIMARY KEY NOT NULL,
    id_parent INTEGER references tbEnumeration (id_tblDirectory) DEFAULT NULL,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    unique (code)
    );
"""



with sqlite3.connect(db_name, isolation_level=None) as conn:
    conn.execute("DROP TABLE IF EXISTS tblDirectory;")
    conn.execute(query)

query_enum_1 = """
    CREATE TABLE prices (
        id         INTEGER                                PRIMARY KEY,
        pName      TEXT CHECK( LENGTH(pName) <= 100 )     NOT NULL DEFAULT '',
        pType      TEXT CHECK( pType IN ('M','R','H') )   NOT NULL DEFAULT 'M',
        pField     TEXT CHECK( LENGTH(pField) <= 50 )     NULL DEFAULT NULL,
        pFieldExt  TEXT CHECK( LENGTH(pFieldExt) <= 50 )  NULL DEFAULT NULL,
        cmp_id     INTEGER                                NOT NULL DEFAULT '0'
);
"""

query_enum_2 = """
PRAGMA foreign_keys = ON;

CREATE TABLE Price (
  PriceId INTEGER       PRIMARY KEY AUTOINCREMENT NOT NULL,
  Name    VARCHAR(100)  NOT NULL,
  Type    CHAR(1)       NOT NULL DEFAULT ('M') REFERENCES PriceType(Type)
);

CREATE TABLE PriceType (
  Type    CHAR(1)       PRIMARY KEY NOT NULL,
  Seq     INTEGER
);

INSERT INTO PriceType(Type, Seq) VALUES ('M',1);
INSERT INTO PriceType(Type, Seq) VALUES ('R',2);
INSERT INTO PriceType(Type, Seq) VALUES ('H',3);
"""
q_3 = """
    CREATE TABLE product (
        product_id      INTEGER PRIMARY KEY,
        product_Name    TEXT CHECK( LENGTH(product_Name) <= 50 ) NOT NULL DEFAULT '',
        product_Type    TEXT CHECK( product_Type IN ('A','B','C')) NOT NULL DEFAULT 'A',
        product_Field   TEXT CHECK( LENGTH(product_Field) <= 40 ) NULL DEFAULT NULL,
        product_Version TEXT CHECK( LENGTH(product_Version) <= 50 ) NULL DEFAULT NULL,
        company_id      INTEGER NOT NULL DEFAULT '11'
);

"""
