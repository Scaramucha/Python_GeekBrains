my_list = []
for i in range(0, 1001):
    my_list.append(i)
for i in my_list:
    if i % 2 == 0:
        my_list.remove(i)
for i in range(len(my_list)):
    my_list[i] = my_list[i] ** 3
sum_list = []
for i in my_list:
    sum_numb = 0
    while i != 0:
        sum_numb = sum_numb + i % 10
        i = i // 10
    sum_list.append(sum_numb)
numbers = []
a = 0
for i in sum_list:
    if i % 7 == 0:
        numbers.append(a)
        a = a + 1
    else:
        a = a + 1
main_sum = 0
for i in numbers:
    main_sum = main_sum + my_list[i]
print(main_sum)
for i in range(len(my_list)):
    my_list[i] = my_list[i] + 17
sum_list = []
for i in my_list:
    sum_numb = 0
    while i != 0:
        sum_numb = sum_numb + i % 10
        i = i // 10
    sum_list.append(sum_numb)
numbers = []
a = 0
for i in sum_list:
    if i % 7 == 0:
        numbers.append(a)
        a = a + 1
    else:
        a = a + 1
main_sum = 0
for i in numbers:
    main_sum = main_sum + my_list[i]
print(main_sum)

# Не сильно поняла цель пункта b и *. Т.е. по факту я работаю с теми же списками, что и в a.
# По факту b и * получились копипаст. Или надо решить задачу без вспомогательных списков?