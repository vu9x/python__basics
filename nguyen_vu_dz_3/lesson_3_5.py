from random import choice


def get_jokes(number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
    number_of_jokes = [] * number

    for i in range(number):
        number_of_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return number_of_jokes


print(get_jokes(2))
