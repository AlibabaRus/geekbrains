from time import perf_counter


class TrafficLight:
    def __init__(self, color):
        self.color = color
        self.running()


    def running(self):
        if self.color == 'красный':
            print('Ждите, сейчас горит красный!')
            start = perf_counter()
            while perf_counter() - start < 7:
                pass
            self.color = 'жёлтый'
            print('Приготовьтесь, сейчас горит жёлтый!')
            start = perf_counter()
            while perf_counter() - start < 2:
                pass
            self.color = 'зелёный'
            print('Можете идти, сейчас горит зелёный!')

situation = TrafficLight('красный')