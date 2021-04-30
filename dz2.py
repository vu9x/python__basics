class ZeroError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


a = 5
b = 0

try:
    ab = a / b
except ZeroDivisionError:
    raise ZeroError('Ошибка деления на ноль')
