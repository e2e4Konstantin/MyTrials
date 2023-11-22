t = ('kV·A, кВА, kVA', 'кВ•А, кВА, ква')
r = []
for x in t:
    r.extend(x.split(','))
print(r)

d = [x.split(',') for x in t]
print(d)

from itertools import chain

print(list(chain.from_iterable([x.split(',') for x in t])))