import sys
import pprint
import inspect
import os

import utils_0.features
import utils_0.defines

# import heap.hdef
# import heap.cats_heap
from heap import Cat, my_cat


def main():
    print(f'{__name__}')
    print(sys.builtin_module_names)
    pprint.pprint(f'{sys.path=}\n{sys.meta_path=}')
    print(f'{dir()=}')

    modules = inspect.getmembers(pprint)
    results = filter(lambda m: inspect.ismodule(m[1]), modules)
    for o in results:
        print('The list of imported Python modules are :', o)

    print(sys.modules.keys())
    print(inspect.getfile(os))
    # print(f'{dir()=}')
    # print(f'>> {pprint.__dict__["pprint"]=}\n {sys.argv=}')


def get_dogs():
    utils_0.features.my_dog()
    m = utils_0.defines.Dog("Zuchka")
    m.sound()


# def get_cats():
#     heap.cats_heap.my_cat()
#     m = heap.hdef.Cat("Murka")
#     m.sound()

def get_cats():
    my_cat()
    m = Cat("Murka")
    m.sound()


if __name__ == '__main__':
    # main()
    get_dogs()
    get_cats()
