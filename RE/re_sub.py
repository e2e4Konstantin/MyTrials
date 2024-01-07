import re

# x = re.sub(r'([a-z]+)( .+)', r'\2 \1', 'python язык программирования')  
    # # ' язык программирования python'
    # # \2 — это группа символов ( .+)
    # # \1 — это группа символов ([a-z]+)
# print(x)

# x = re.sub(r'(?P<lang>[a-z]+)(?P<more> .+)', r'\g<more> \g<lang>', 'python язык программирования')  
# print(x)

# x = re.sub(r'([a-z]+)( .+)', r'\g<2> \g<1>', 'python язык программирования')  
# print(x)

# x = re.sub(r'[а-яФ-Яa-zA-Z\s]\.{2}', '', 'абр......a.')  
# print(x)

dot = re.compile(r"[а-яФ-Я\w\s-]\.{2}")

x = dot.sub('', 'абD..р...a.')  
print(x)


x = re.sub('\.', '', '.......')  
print(x) if x else print(None)

double_dot = re.compile(r"[а-яФ-Я\w\s-]\.{2}")
    dot = re.compile(r"\.")

while double_dot.search(src_line):
    src_line = double_dot.sub('', src_line)
    
while dot.search(src_line):
    src_line = dot.sub("", src_line)        

