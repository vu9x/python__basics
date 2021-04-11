import json

# user_dic = {}
with open('users.csv', 'r', encoding='utf-8-sig') as users, \
        open('hobby.csv', 'r', encoding='utf-8-sig') as hobby, \
        open('dictionary.txt', 'w', encoding='utf-8') as dictionary:
    # for u, h in zip(users, hobby):
    #     user_dic.update({u.strip().replace(',', ' '): h.strip()})
    user_dic = {u.strip().replace(',', ' '): h.strip() for u, h in zip(users, hobby)}
    json.dump(user_dic, dictionary)

print(user_dic)

with open('dictionary.txt', 'r', encoding='utf-8') as f:
    new_dic = json.load(f)
    print(new_dic)
