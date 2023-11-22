import collections
import sqlite3
import time
import random
import os

from collections import defaultdict
from random import randint

if os.path.isfile('test.db'):
    os.unlink('test.db')

db = sqlite3.connect('test.db', isolation_level=None)

# Build our database
# nNames is the size of the  "names"  space
# nSymbol is the size of the "symbol" space
# nRows is the number of rows to create

nNames  =     100
nSymbol =  100000
nRows   = 5000000

rs = chr(30)
fs = chr(31)

print(f"nNames = {nNames}; nSymbol = {nSymbol}; nRows = {nRows}")

ascii = list(c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def randomlist(size):
    from random import shuffle
    a = []
    for i in range(size):
        shuffle(ascii)
        a.append(''.join(ascii[:8]))
    return a

st = time.time()
nameList = randomlist(nNames)
symbolList = randomlist(nSymbol)

print(f"Random lists created in {round(time.time()-st,3)} seconds")

db.executescript("create table enum(name text not null, symbol text not null, primary key(name, symbol))")

st = time.time()
lNames = nNames - 1
lSymbols = nSymbol - 1
db.executescript('begin')
for i in range(nRows):
    db.execute('insert or ignore into enum values (?,?)', (nameList[randint(0, lNames)], symbolList[randint(0, lSymbols)]))
db.execute('commit')
print(f"Database Build Complete; {nRows} in {round(time.time()-st,3)} seconds")
print(f"Table enum contains {db.execute('select count() from enum').fetchone()[0]} rows")
print()

# retrieve the data one by each an build an in-memory structure

print("Building internal data structure method simple")

sql = """ select name, symbol from enum order by rowid; """
data = None
st = time.time()
data = defaultdict(list)
for row in db.execute(sql):
    data[row[0]].append(row[1])
for key in data.keys():
    data[key] = tuple(data[key])
print(f"Internal Structure built in {round(time.time()-st, 3)} seconds")
print()
data = None

# retrieve the data in "diddled" form

print("Building internal data structure diddling the data so there is one row per name")

sql = """
select name, (select group_concat(symbol,char(31))
from (select symbol from enum where name == o.name order by rowid)) as symbols
      from ( select distinct name from enum order by rowid) as o
"""
data = {}
st = time.time()
for row in db.execute(sql):
    data[row[0]] = tuple(row[1].split(fs))
print(f"Internal Structure built in {round(time.time()-st, 3)} seconds")
print()
