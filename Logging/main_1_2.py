import os
import sys
sys.path.append('Logging')

from mod_2 import mod_2
from mod_1 import mod_1


def main():
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # cwd = os.getcwd()
    # x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(dir_path, cwd, x, sep='\n | ')
    # print(__package__)
    # if __name__ == "__main__" and __package__ is None:

    mod_1()
    mod_2()


if __name__ == "__main__":

    main()
