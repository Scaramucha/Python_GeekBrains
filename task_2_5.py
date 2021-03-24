main_price = [11.05, 45.9, 39.99, 34, 66.6, 6.66, 0.59, 77.35, 88.8, 999.58, 1000, 555, 666, 888]
price = main_price.copy()
count = 0
for i in price.copy():
    format_price = []
    rub = int(i * 100 // 100)
    cop = int(i * 100 % 100)
    format_price.append(rub)
    format_price.append(cop)
    price[count] = format_price
    count += 1
for rub, cop in price:
    if rub != price[-1][0]:
        a = f'{rub} руб {cop:02d} коп,'
    else:
        a = f'{rub} руб {cop:02d} коп'
    print(a, end=" ")
# я знаю, я написала странное, но я не нашла, как заставить end работать в f-строках.
# И как заставить их заменить перенос строки на символ, при взятитии данных из списка в списке тоже не нашла.
main_price.sort()
print(main_price)
# Или у меня, или у пайшарма крышечка поехала. При том я проверила на трёх компах. Два арча манджарика и ксубунту.
# при прогоне 20, 21 строки в упор не видит. даже если я в принт напишу "hello".
# Но вот я делаю копипаст этих же строк и... всё работет.
main_price.sort()
print(main_price)
main_price_sort_min = main_price
main_price_sort_min.sort(reverse=True)
print(main_price_sort_min)
number_of_price = 0
while number_of_price < 5:
    print(main_price.pop(0))
    number_of_price += 1