import os
import sys


# def get_base_dir():
#     return os.path.relpath(sys.argv[0])


def get_base_dir():
    if getattr(sys, 'frozen', False):
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return BASE_DIR


if __name__ == '__main__':
    print(get_base_dir())
