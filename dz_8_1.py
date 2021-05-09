import re


def email_parse(email):
    email_dict = {}
    name_format = re.compile(r'^\w+')
    domain_identifier = re.compile(r'^\w+@[a-z]+\.[a-z]+$')
    domain_format = re.compile(r'[a-z]+\.[a-z]+$')
    try:
        chek = domain_identifier.fullmatch(email)
        if chek is None:
            raise ValueError
        email_dict['name'] = name_format.findall(email)[0]
        email_dict['domain'] = domain_format.findall(email)[0]
        print(email_dict)
    except ValueError as e:
        print(f'{e}: wrong email: {email}')


email_parse(input("Мыло писать сюда"))
