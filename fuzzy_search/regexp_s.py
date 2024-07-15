import regex
r = regex.match('(amazing){e<=1}', 'amaging')
print(r)

r = regex.search('(test){e<=1}', '123 test')
print(r)


for m in regex.findall('(manhattan){e<2}', "thelargemanhatanproject is a great project in themanhattincity"): 
    print(m)


text = 'I went to see Dr. House. The date was 2021-2-04. It cost 60 euros.'
specimen = '2020-02-05'
pattern = specimen.replace('-', r'\-')
fuzzy_pattern = f'({pattern})' + '{s<=3,i<=3,d<=3}'

match = regex.search(fuzzy_pattern, text, regex.BESTMATCH)
print(match)

ls = "Раздел II. Стоимостные показатели по объектам"
qs = "Раздел"

match = regex.search("Раздел{e<1}", ls, regex.BESTMATCH)
print(match)

match = regex.findall("Раздел", ls, regex.BESTMATCH)
print(match)

match = regex.findall("Раздел{e<2}", ls)
print(match)