from itertools import zip_longest


with open('users.csv', 'r', encoding='utf-8')as user_f:
    users_list = user_f.read().splitlines()
with open('hobby.csv', 'r', encoding='utf-8')as hobby_f:
    hobby_list = hobby_f.read().splitlines()


def more():
    exit(1)


def less_or_equally():
    with open('users_hobby.txt', 'w', encoding='utf-8')as f:
        text = zip_longest(users_list, hobby_list)
        for name, hobby in text:
            string_to_write = f'{name} : {hobby} \n'
            f.write(string_to_write)


def select_func():
    if len(users_list) >= len(hobby_list):
        less_or_equally()
    else:
        more()


select_func()
