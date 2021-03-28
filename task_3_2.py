def num_translate_adv(a=input("Введите значение")):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    rus = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
    if a.lower() in eng:
        index_element = eng.index(a.lower())
        if a.islower():
            print(rus[index_element])
        else:
            print(rus[index_element].title())
    elif a.lower() in rus:
        index_element = rus.index(a.lower())
        if a.islower():
            print(eng[index_element])
        elif a.istitle():
            print(eng[index_element].title())
    else:
        print(None)


num_translate_adv()
