# Необходимо его обработать — обособить каждое целое число
# (вещественные не трогаем) кавычками (добавить кавычку до и
# кавычку после элемента списка, являющегося числом) и дополнить
# нулём до двух целочисленных разрядов:

text_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
text_2 = []

for element in text_1:
    try:
        if isinstance(int(element), int):
            if "+" in element:
                new_element = f'"+{int(element):02d}"'
            else:
                new_element = f'"{int(element):02d}"'
            text_2.append(new_element)
    except ValueError:
        text_2.append(element)

sentence = ' '.join(text_2)
print(sentence)
