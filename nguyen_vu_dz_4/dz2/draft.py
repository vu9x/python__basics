from requests import get
import xml.etree.ElementTree as Et

# Получаем веь сайт
response = get('http://www.cbr.ru/scripts/XML_daily.asp')

# Получаем весь xml файл как строку
root = Et.fromstring(response.content)

user_answer = input('Пожалуйста, введите желаемую валюту, программа выдаст курс валюты: ')

exchange_dic = {}

# Парсим из xml файла нужные нам значения тэгов: код валюты, курс валют
for valute in root.findall('Valute'):
    char_code = valute.find('CharCode').text
    value_str = valute.find('Value').text.replace(',', '.')
    value_float = float(value_str)

    exchange_dic.update({char_code: value_float})  # Создаем словарь со значениями Валюта: Курс

# Получаем нужный курс валют
if exchange_dic.get(user_answer.upper()):
    print(f'{user_answer.upper()}: {exchange_dic.get(user_answer.upper())}')
