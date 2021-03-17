duration = int(input("Введите время в секундах"))
day = duration // 86400
hour = (duration % 86400) // 3600
minute = ((duration % 86400) % 3600) // 60
second = ((duration % 86400) % 3600) % 60
if day == 0 and hour == 0 and minute == 0:
    print("{:02d}" '{}'. format(second, "сек"))
elif day == 0 and hour == 0 and minute > 0:
    print("{:02d}" '{}' "{:02d}" '{}'.format(minute, "мин ", second, "сек"))
elif day == 0 and hour > 0:
    print("{:02d}" '{}' "{:02d}" '{}' "{:02d}" '{}'.format(hour, "час ", minute, "мин ", second, "сек"))
elif day > 0:
    print("{:02d}" '{}' "{:02d}" '{}' "{:02d}" '{}' "{:02d}" '{}'.format(day, "дн ", hour, "час ", minute, "мин ", second, "сек"))
