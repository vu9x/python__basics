class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surmane = surname
        self.position = position
        self._salary = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.position}: {self.name} {self.surmane}'

    def get_total_income(self):
        return self._salary["wage"] + self._salary["bonus"]


worker_1 = Position('John', 'Don', 'manager', 5, 10)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
