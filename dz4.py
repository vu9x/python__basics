class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police is True:
            self.is_police = True
        else:
            self.is_police = False

    def go(self):
        return print('Машина поехала')

    def stop(self):
        return print('Машина остановилась')

    def turn(self, direction):
        return print(f'Машина повернула на {direction}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Ваша скорость {self.speed}. Вы превысли скорость'
        else:
            return f'Ваша скорость {self.speed}.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Ваша скорость {self.speed}. Вы превысли скорость'
        else:
            return f'Ваша скорость {self.speed}.'


class PoliceCar(Car):
    pass


work_car1 = WorkCar(41, 'red', 'bmw', False)
print(work_car1.show_speed(), work_car1.name, work_car1.color, work_car1.is_police)
