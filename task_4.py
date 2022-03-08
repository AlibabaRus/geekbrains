class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} поехала на{direction}!')

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышен лимит скорости на {self.speed - 60} км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышен лимит скорости на {self.speed - 40} км/ч!')


class PoliceCar(Car):
    pass


auto_1 = TownCar(80, "Чёрный" , "BMW")
auto_1.show_speed()
