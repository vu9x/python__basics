# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной
# буквы — результат тоже должен быть с заглавной.


def num_translate(num):
    """EN-RU dictionary for digits 0-9"""
    en_ru_dic = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыри',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять'
    }
    if isinstance(num, str) and num.istitle():
        return en_ru_dic.get(num.lower()).title()
    elif isinstance(num, str):
        return en_ru_dic.get(num)
    else:
        return None


print(num_translate('one'))
print(num_translate('One'))
print(num_translate(0))
print(help(num_translate))
