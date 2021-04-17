import sys
from itertools import islice


def give_me_from(show_from_this):
    show_from_this -= 1
    with open('bakery.csv', 'r', encoding='utf-8')as f:
        file = f.readlines()
        lines = list(islice(file, show_from_this, None))
        return lines

def show_me_from(number):
    show_from_this = int(number)
    print(*give_me_from(show_from_this))


if __name__ == '__main__':
    _script_name, start_element = sys.argv
    show_me_from(start_element)
