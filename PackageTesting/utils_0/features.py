import utils_0.defines


def my_dog():
    p = utils_0.defines.Dog()
    p.sound()



if __name__ == "__main__":
    my_dog()
    print(f"{__name__ = }")
else:
    print(f"features.py>> {__name__}")