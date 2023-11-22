# import heap.hdef
from heap.hdef import Cat

# def my_cat():
#     p = heap.hdef.Cat()
#     p.sound()


def my_cat():
    p = Cat()
    p.sound()




if __name__ == "__main__":
    my_cat()
    print(f"{__name__ = }")
else:
    print(f"cats_heap.py>> {__name__}")
