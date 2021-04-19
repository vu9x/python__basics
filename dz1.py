import re


def email_check(email):
    RE_EMAIL = re.compile(r'(?:[a-zA-Z0-9]+)@(?:[a-zA-Z0-9]+)\.[a-zA-Z]+')

    if RE_EMAIL.match(email):
        return True
    else:
        assert RE_EMAIL.match(email), f'ValueError: wrong email: {email}'


def email_parse(email):
    email_dic = {}
    if email_check(email):
        RE_USER_NAME = re.compile(r'^\w+')
        RE_COMPANY_NAME = re.compile(r'@(\w+.\w+)')
        email_dic.update({'username': RE_USER_NAME.search(email).group(0),
                          'domain': RE_COMPANY_NAME.search(email).group(1)})
        return email_dic
    else:
        return None


wrong_email = 'someone@gee kbrains.ru'
right_email = 'someone@geekbrains.ru'
print(email_parse(right_email))
print(email_parse(wrong_email))
