new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers_list = []
for i in new_list:
    list_of_words = list(i)
    for x in list_of_words:
        if x.isdigit():
            numbers_list.append(i)
            break
reverse_index = len(new_list) * (-1)
for i in new_list.copy():
    if i in numbers_list:
        new_list.insert(reverse_index, '"')
        new_list.insert(reverse_index + 1, '"')
        reverse_index += 1
    else:
        reverse_index += 1
for i in range(len(new_list)):
    if new_list[i] in numbers_list:
        a = list(new_list[i])
        if len(a) < 2:
            new_list[i] = "0" + new_list[i]
        elif len(a) == 2 and a[0].isdigit() == False:
            a.insert(1, "0")
            new_list[i] = "".join(a)
print(" ".join(new_list[0:1]), "".join(new_list[1:4]), " ".join(new_list[4:5]), "".join(new_list[5:8]), " ".join(new_list[8:12]), "".join(new_list[12:15]), " ".join(new_list[15:16]))

