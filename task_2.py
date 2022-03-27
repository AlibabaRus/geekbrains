from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def __init__(self, v, h):
        self._v = v / 6.5 + 0.5
        self._h = 2 * h + 0.3

    @abstractmethod
    def get_quantity(self):
        pass


class Clothes(AbstractClass):
    @property
    def get_quantity(self):
        return self._v + self._h


client_1 = Clothes(50, 60)
print(client_1.get_quantity)
