class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title}: запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'{self.title}: запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title}: запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return f'{self.title}: запуск отрисовки маркером'


s_paint = Stationery('Рисунок')
print(s_paint.draw())

pen_paint = Pen('Рисунок ручкой')
print(pen_paint.draw())

pencil_paint = Pencil('Рисунок карандашом')
print(pencil_paint.draw())

handle_paint = Handle('Рисунок маркером')
print(handle_paint.draw())
