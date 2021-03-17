number = int(input("Число процентов от 1 до 20"))
percent = ["процент", "процента", "процентов"]
if number == 1:
    print(number, percent[0])
elif number in [2, 3, 4]:
    print(number, percent[1])
else:
    print(number, percent[2])
