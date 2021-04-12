from requests import get
URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.writelines(get(URL, stream=True).text)
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    remote_add = [element.split()[0] for element in f.read().splitlines()]
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    request_type = [element.split()[5].replace('"', '') for element in f.read().splitlines()]
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    requested_resource = [element.split()[6] for element in f.read().splitlines()]
information = list(zip(remote_add, request_type, requested_resource))
print(information[0])
print(information[-1])