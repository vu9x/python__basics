# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


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
    return en_ru_dic.get(num)


print(num_translate('one'))
print(num_translate(0))
print(help(num_translate))
