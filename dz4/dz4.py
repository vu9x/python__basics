from itertools import zip_longest


with open('users.csv', 'r', encoding='utf-8-sig') as users, \
        open('hobby.csv', 'r', encoding='utf-8-sig') as hobby, \
        open('users_hobby.txt', 'w', encoding='utf-8') as dictionary:
    for user, hob in zip_longest(users, hobby):
        if user is None:
            exit(1)
        else:
            if hob is not None:
                dictionary.writelines(f'{user.strip().replace(",", " ")}: {hob.strip()}\n')

with open('users_hobby.txt', 'r', encoding='utf-8') as f:
    print(f.readlines())
