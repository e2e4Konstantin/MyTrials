from fuzzysearch import find_near_matches
# search for 'PATTERN' with a maximum Levenshtein Distance of 1

r = find_near_matches('PATTERN', '---PATERN---', max_l_dist=1)
print(r)

r = find_near_matches('PATTERN', '---PATERN---', max_l_dist=1, max_deletions=0)
print(r)

# note that a deletion + insertion may be combined to match a substution
r =  find_near_matches('PATTERN', '---PAT-ERN---', max_deletions=1, max_insertions=1, max_substitutions=0)
print(r) # the Levenshtein distance is still 1

# ... but deletion + insertion may also match other, non-substitution differences
r=find_near_matches('PATTERN', '---PATERRN---', max_deletions=1, max_insertions=1, max_substitutions=0)
print(r)


ls = "РазделII. Стоимостные показатели по объектам"
qs = "Раздел"
r=find_near_matches(qs, ls, max_deletions=1, max_insertions=1, max_substitutions=0)
print(r)
