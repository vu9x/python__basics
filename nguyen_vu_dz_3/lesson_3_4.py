# в разработке задача

def thesaurus_adv(*args):
    name_dic = {}
    for i in args:
        first_last_names = i.split(' ')
        if name_dic.get(first_last_names[1][0]):
            name_dic.setdefault(first_last_names[1][0], first_last_names[1][0].append(i))
        else:
            name_dic.update({first_last_names[1][0]: i})


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

"""
def thesaurus(*args):
    name_dic = {}
    for name in args:
        if name_dic.get(name[0]):
            name_dic.update({name[0]: [name_dic.pop(name[0]), name]})
        else:
            name_dic.update({name[0]: name})

    return name_dic
"""