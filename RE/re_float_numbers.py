# Regular expression for floating point numbers

"[+-]?([0-9]*[.])?[0-9]+"
"[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)"
"^[+-]?([0-9]*[.])?[0-9]+$"
"[+-]?((\d+\.?\d*)|(\.\d+))"


"[+-]?(\d+([.]\d*)?(e[+-]?\d+)?|[.]\d+(e[+-]?\d+)?)"

"[+-]?(\d+([.]\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)"



import re

def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    float regex comes from https://stackoverflow.com/a/12643073/190597
    '''
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]

alist=[
    "something1",
    "something2",
    "something1.0",
    "something1.25",
    "something1.105"]

alist.sort(key=natural_keys)
print(alist)

