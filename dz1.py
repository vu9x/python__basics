def odd_gen(start=1, end=1):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number


for i in odd_gen(1, 15):
    print(i)
