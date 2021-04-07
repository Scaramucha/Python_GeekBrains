tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Маша', 'Рая', 'Дима']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

while len(klasses) < len(tutors):
    klasses.append(None)

person = (element for element in zip(tutors, klasses))
print(next(person))
print(next(person))
print(next(person))
print(*person)
