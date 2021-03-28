def num_translate(a=input("Введите значение")):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    rus = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
    if a in eng:
        index_element = eng.index(a)
        print(rus[index_element])
    elif a in rus:
        index_element = rus.index(a)
        print(eng[index_element])
    else:
        print(None)


num_translate()
