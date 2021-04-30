class WareHouse:
    def __init__(self, rows_list, height, width, employee):
        self.size = height * width
        self.number_of_rows = rows_list
        self.employee = employee


class Devices:
    def __init__(self, device_name, device_code):
        self.device_name = device_name
        self.device_code = device_code


class Printer(Devices):
    def __init__(self, price, quantity, device_name, device_code):
        self.price = price
        self.quantity = quantity
        super().__init__(device_name, device_code)


class Scanner(Devices):
    def __init__(self, price, quantity, device_name, device_code):
        self.price = price
        self.quantity = quantity
        super().__init__(device_name, device_code)


class Xerox(Devices):
    def __init__(self, price, quantity, device_name, device_code):
        self.price = price
        self.quantity = quantity
        super().__init__(device_name, device_code)
