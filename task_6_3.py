with open('users.csv', 'r', encoding='utf-8')as user_f:
    users_list = user_f.read().splitlines()
with open('hobby.csv', 'r', encoding='utf-8')as hobby_f:
    hobby_list = hobby_f.read().splitlines()
my_dict = {}


def less_or_equally():
    count_index_hobby = 0
    for name in users_list:
        if count_index_hobby < len(hobby_list):
            my_dict[name] = hobby_list[count_index_hobby]
            count_index_hobby += 1
        else:
            my_dict[name] = None


def more():
    exit(1)


def select_fuction():
    if len(users_list) >= len(hobby_list):
        less_or_equally()
    else:
        more()


select_fuction()
print(my_dict)
