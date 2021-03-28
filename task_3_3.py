def thesaurus_adv(*args):
    names = args
    names_dict = {}
    for i in names:
        if i[0] not in names_dict.keys():
            names_dict[i[0]] = []
            names_dict[i[0]].append(i)
        elif i[0] in names_dict.keys():
            names_dict[i[0]].append(i)
    return names_dict


print(thesaurus_adv('Татьяна', 'Ульяна', 'Михаил', 'Анатолий', 'Наталья', 'Нииколай', 'Альбина'))
