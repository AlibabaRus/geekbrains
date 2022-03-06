import re


def email_parse(email_address):
    pattern = re.compile(r'(?P<username>\w+)[@](?P<domain>\w+\.\w+)')
    if len(pattern.findall(email_address)) == 1:
        for item in pattern.finditer(email_address):
            print(item.groupdict())
    else:
        print(f'ValueError: wrong email: {email_address}')
        raise ValueError
email_parse(input())