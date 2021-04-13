import sys


def sum_to_add(adding_sum=input('')):
    with open('bakery.csv', 'a', encoding='utf-8')as f:
        f.write(f'{adding_sum} \n')


if __name__ == '__main__':
    _script_name, new_sum = sys.argv
    sum_to_add(new_sum)
