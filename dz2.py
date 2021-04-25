from abc import ABC, abstractmethod


class Clothers(ABC):
    @abstractmethod
    def calc_fabric_consumption(self):
        pass


class Coat(Clothers):
    def __init__(self, v):
        self.v = v

    @property
    def calc_fabric_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothers):
    def __init__(self, h):
        self.h = h

    @property
    def calc_fabric_consumption(self):
        return self.h * 2 + 0.3


if __name__ == '__main__':
    c = Coat(5)
    s = Suit(4)
    print(c.calc_fabric_consumption)
    print(s.calc_fabric_consumption)
