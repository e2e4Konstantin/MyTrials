from typing import Literal, get_args

_TYPES = Literal["solar", "view", "both"]

def func(a, b, c, type_: _TYPES = "solar"):
    options = get_args(_TYPES)
    assert type_ in options, f"'{type_}' is not in {options}"


assert sim_types in ['solar', 'view', 'both'], 'sim type parameter must be solar, view or both'


def func(a, b, c, **kw):
    if kw.get('do_solar'):
        # Do Solar
    if kw.get('do_view'):
        # Do view


def func(a, b, c, *args):
    for arg in args:
        arg(a, b, c)

def foosim(a, b, c):
    print 'foosim %d' % (a + b + c)

def barsim(a, b, c):
    print 'barsim %d' % (a * b * c)



def example_function(a, b, c, op='add'):
    return {'add': a+b+c, 'multiply': a*b*c}[op]


example_function(0, 1, 2, 'add') # returns 3
example_function(0, 1, 2, 'multiply') # returns 0
