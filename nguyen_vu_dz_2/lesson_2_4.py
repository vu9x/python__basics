genuine_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                'токарь высшего разряда нИКОЛАй', 'директор аэлита']

name_list = []
for text in genuine_list:
    word_list = text.split(" ")
    name = word_list.pop(-1).title()

    name_list.append(name)
    word_list.append(name)

    sentence = ' '.join(word_list)
    genuine_list[genuine_list.index(text)] = sentence

print(genuine_list)

for user in name_list:
    print(f'Приве, {user}')
