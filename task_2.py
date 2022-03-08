class Road:
    def __init__(self, length, width, mass, depth):
        self._length = length
        self._width = width
        self._mass = mass
        self._depth = depth

    def result(self):
        print(
            f'{self._length} м*{self._width} м*{self._mass} кг*{self._depth} см = {self._length * self._width * self._mass * self._depth // 1000} т')


situation = Road(20, 5000, 25, 5)
situation.result()
