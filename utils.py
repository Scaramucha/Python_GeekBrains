from requests import get
from datetime import date


def currency_rates(currency_name):
    currency_name = currency_name.upper()
    url_addres = 'http://www.cbr.ru/scripts/XML_daily.asp'
    content = get(url_addres).text
    sorted_content = content.split('><')
    nominal = []
    char_code = []
    value = []
    today = []

    for member in sorted_content:
        date_saving = []
        if 'Date' in member:
            for i in member:
                if i.isdigit() is True or i == ".":
                    date_saving.append(i)
            today.append("".join(date_saving))

    calendar = "".join(today).split('.')

    for member in sorted_content:
        saving_nominal = []
        if 'Nominal' in member:
            for i in member:
                if i.isdigit() is True:
                    saving_nominal.append(i)
            nominal.append("".join(saving_nominal))

    for member in sorted_content:
        saving_value = []
        if 'Value' in member:
            for i in member:
                if i.isdigit() is True or i == ",":
                    saving_value.append(i)
            value.append("".join(saving_value))

    for member in sorted_content:
        saving_char_code = []
        if 'CharCode' in member:
            for i in member:
                if i.istitle() is True:
                    saving_char_code.append(i)
            char_code.append("".join(saving_char_code[2:-2]))

    information = list(zip(nominal, value, char_code))
    structured_information = {}
    for element in information:
        structured_information[element[-1]] = [element[0], element[1]]

    day, month, year = int(calendar[0]), int(calendar[1]), int(calendar[2])
    date_for_today = date(year, month, day)

    if currency_name in structured_information:
        print(f'Сегодня {date_for_today}. Курс заданной валюты {structured_information[currency_name][1]} руб. за',
              f'{structured_information[currency_name][0]} ед.')
    else:
        print(None)
