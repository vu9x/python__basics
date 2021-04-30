class NotInt(ValueError):
    def __init__(self, txt):
        self.txt = txt


list_int = []

while True:
    user_input = input("Введите число: ")
    if user_input.lower() == "stop":
        print(f'Вы ввели следующие числа: {list_int}')
        break

    try:
        list_int.append(int(user_input))
    except ValueError:
        raise NotInt('Вы ввели не число')

    # Прошу прощения. Не очень понимаю как сделать кастомное исключение,
    # чтобы программа продолжала работать
