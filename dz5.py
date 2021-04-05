src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_number = set()
tmp = set()

for el in src:
    if el not in tmp:
        unique_number.add(el)
    else:
        unique_number.discard(el)
    tmp.add(el)

result = [el for el in src if el in unique_number]
print(result)
