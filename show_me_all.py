def give_me_all():
    with open('bakery.csv', 'r', encoding='utf-8')as f:
        information = f.readlines()
        return information


def show_me_all():
    print(*give_me_all())


if __name__ == '__main__':
    show_me_all()
