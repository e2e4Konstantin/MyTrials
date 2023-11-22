import re
retype = type(re.compile('hello, world'))

print(retype)
print(isinstance(re.compile('goodbye'), retype))

# p: re.Pattern = "\d+"

if hasattr(possibly_a_re_object, "match"): # Treat it like it's an re object
    possibly_a_re_object.match(thing_to_match_against)
else:
    pass
    
# re. match() searches for matches from the beginning of a string 
# while re.search() searches for matches anywhere in the string.    


p = re.compile(r"^\s*(\d+)(\.\d+)")
p.search("  3.155-1-1-0-1").group()
'  3.155'
p.search("  3.155-1-1-0-1").groups()
('3', '.155')




d2 = r"(\d+)"
d3 = r"[^\D]"
d4 = r"(?:[0-9]{1,2}[-|/|.]){2}[0-9]{2,4}"
RE_DIGITS = r"(\d+)"

# # s="4dd edwed34r5 ,5 "
# # s="45"
# s="1.2.23, 15.2.23"


s="4dd edwed34r5 ,5 "
w = re.findall(RE_DIGITS, s.strip())
print(w)

a = lambda x: re.findall(RE_DIGITS, x.strip()) is not None
print(a(" 01 23 45 6789 "))




# p = re.compile(d4)
# r = p.search(s)
# print(r)
# w = p.findall(s)
# print(w)


# match = re.fullmatch(d4, s.strip())
# print('YES' if match else 'NO') 

# print(match, type(match))



# # print(match is None)
# # print(r)

# a = lambda x: re.fullmatch(RE_DIGITS, x.strip()) is not None
# print(a(" 01 23 45 6789 "))



# a = lambda x: re.findall(RE_DIGITS, x.strip()) is not None
# print(a("0"))    