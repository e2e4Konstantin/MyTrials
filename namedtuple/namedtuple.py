from collections import namedtuple


DirectoryItem = namedtuple(typename="DirectoryItem", field_names=['id', 'item_name', 'directory_name'])
DirectoryItem.__annotations__ = {'id': int, 'item_name': str, 'directory_name': str}

if __name__ == '__main__':
    from icecream import ic

    x = DirectoryItem(1, 'chapter', 'quotes')
    ic(x)
    ic(DirectoryItem.__annotations__)

    p = namedtuple('Point', 'x,y', defaults=(1,))
    p.__annotations__ = {'x': int, 'y': int}

    a = p(5,9)
    ic(a)
    ic(p.__annotations__)