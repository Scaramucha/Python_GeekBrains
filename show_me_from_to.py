import sys
from itertools import islice


def give_me_from_to(show_from_this, to_this):
    show_from_this -= 1
    with open('bakery.csv', 'r', encoding='utf-8')as f:
        file = f.readlines()
        lines = list(islice(file, show_from_this, to_this))
        return lines


def show_me_from_to(show_from_this, to_this):
        show_from_this = int(show_from_this)
        to_this = int(to_this)
        print(*give_me_from_to(show_from_this, to_this))


if __name__ == '__main__':
    _script_name, start, finish = sys.argv
    show_me_from_to(start, finish)
