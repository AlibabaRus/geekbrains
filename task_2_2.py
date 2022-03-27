#не до конца понял задание, поэтому отправил два варианта
#вариант 2
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def get_quantity(self):
        self._v = self._v / 6.5 + 0.5

    @property
    def get_v(self):
        return self._v


class Coat(AbstractClass):
    def __init__(self, v):
        self._v = v

    @property
    def get_quantity(self):
        return self._v / 6.5 + 0.5


class Suit(AbstractClass):
    def __init__(self, h):
        self._h = h

    @property
    def get_quantity(self):
        return 2 * self._h + 0.3


size_1 = Coat(50)
size_2 = Suit(60)
print(size_1.get_quantity + size_2.get_quantity)
