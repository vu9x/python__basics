# Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего,

# Задание 4 не завершено

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []

for el in src:
    a = src[-len(src)+src.index(el)]
    if el > a:
        result.append(el)
    else:
        result.append(0)
print(result)
