from requests import get
import xml.etree.ElementTree as Et

# Получаем веcь сайт
response = get('http://www.cbr.ru/scripts/XML_daily.asp')

# Получаем весь xml файл как строку
root = Et.fromstring(response.content)


def code_value_dic():
    """ Функция для получения словаря из курсов валют на сайте ЦБ """
    exchange_dic = {}

    # Парсим из xml файла нужные нам значения тэгов {код валюты: курс валют}
    for valute in root.findall('Valute'):
        char_code = valute.find('CharCode').text
        value_str = valute.find('Value').text.replace(',', '.')
        value_float = float(value_str)

        exchange_dic.update({char_code: value_float})  # Создаем словарь со значениями Валюта: Курс

    return exchange_dic


def currency_rates(cur):
    """ Функция для поиска курса валют из словаря code_value_dic() """
    code = cur.upper()

    if code_value_dic().get(cur.upper()):
        value = code_value_dic().get(code)
        # print(f'{code}: {value}')

        return code, value
    else:
        # print(f'Валюта {code} не найдена')
        return None


print(currency_rates('usd'))
print(currency_rates('eur'))
print(currency_rates('eyr'))
