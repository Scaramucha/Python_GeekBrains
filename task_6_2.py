from requests import get
from collections import Counter
URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
with open('nginx_logs.txt', 'w', encoding='utf-8') as file:
    file.writelines(get(URL, stream=True).text)


def find_ip():
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line_list = line.split()
            ip = line_list[0]
            yield ip


def find_spammer(how_much_ip):
    with open('nginx_logs.txt', 'rb'):
        spammer = Counter(find_ip()).most_common(how_much_ip)
        print(spammer)


find_spammer(1)
