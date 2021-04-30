import re


class Data:
    def __init__(self, data):
        RE_DATE = re.compile(r'^(\d{2}[. /-]){2}\d{4}$')
        if RE_DATE.match(data):
            self.data = data

    @classmethod
    def date_month_year(cls, data):
        cls.data = data.split(' ')
        cls.date = int(cls.data[0])
        cls.month = int(cls.data[1])
        cls.year = int(cls.data[2])
        print(cls.date, cls.month, cls.year)

    @staticmethod
    def date_valid(data):
        static_data = data.split(' ')
        if 0 < int(static_data[0]) <= 31:
            print(f'Верный день {static_data[0]}')
        if 0 < int(static_data[1]) <= 12:
            print(f'Верный месяц {static_data[1]}')
        print(f'Год: {static_data[2]}')


d = Data('01 11 2020')
print(d.data)

Data.date_month_year('02 02 2020')
Data.date_valid('03 03 2020')
