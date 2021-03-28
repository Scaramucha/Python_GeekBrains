def thesaurus_adv(*args):
    names = args
    surnames_dict = {}
    for i in names:
        full_name = i.split()
        if full_name[1][0] not in surnames_dict.keys():
            surnames_dict[full_name[1][0]] = {}
            surnames_dict[full_name[1][0]][full_name[0][0]] = []
        elif full_name[1][0] in surnames_dict.keys():
            surnames_dict[full_name[1][0]][full_name[0][0]] = []
    for a in names:
        save = a.split()
        surnames_dict[save[1][0]][save[0][0]].append(a)
    return surnames_dict


print(thesaurus_adv('Татьяна Мышкина', 'Ульяна Кошкина', 'Михаил Котовский',
                    'Анатолий Мышинский', 'Наталья Сизова', 'Нииколай Сазанов',
                    'Альбина Седова', 'Борис Арбузов', 'Антонина Меловая'))
