# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.


def thesaurus(*args):
    name_dic = {}
    for name in args:
        if name_dic.get(name[0]):
            name_dic.update({name[0]: [name_dic.pop(name[0]), name]})
        else:
            name_dic.update({name[0]: name})

    return name_dic



print(thesaurus("Иван", "Мария", "Петр", "Илья"))

"""
def thesaurus2(*args):
    name_dic = {}
    name_list = list(args)
    for name in name_list:
        if name_dic.get(name[0]) is False:
            name_dic.setdefault(name[0], [name])
        else:
            name_dic.update({name[0]: name[0].append(name)})
    return name_dic

print(thesaurus2("Иван", "Мария", "Петр", "Илья"))



thesaurus = ["Иван", "Мария", "Петр", "Илья"]

name_dic = {}
for name in thesaurus:
    name_list = []
    if name_dic.get(name[0]):
        name_dic.update({name[0]: [name_dic.pop(name[0]), name]})
    else:
        name_dic.update({name[0]: name})
return name_dic

print(name_dic)
"""