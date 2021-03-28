def get_jokes(number, flag):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    from random import choice
    if flag == 'Нет' and number <= 5:
        jokes = list(zip(choice([nouns]), choice([adverbs]), choice([adjectives])))
        joke = []
        for i in jokes:
            joke.append(" ".join(i))
        print(joke[:number])
    elif flag == 'Нет' and number > 5:
        print("Тогда я могу предложить тебе только 5 фраз")
    elif flag == 'Да':
        joke = []
        while len(joke) < number:
            jokes = list(zip(choice([nouns]), choice([adverbs]), choice([adjectives])))
            for i in jokes:
                joke.append(" ".join(i))
        print(joke[:number])


get_jokes(int(input("Сколько фраз ты хочешь?")), input("Значения могут повторяться? Да/Нет"))
