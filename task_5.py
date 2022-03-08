class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Получился рисунок: \n ~~~~~')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title} \nПолучился рисунок: \n _____')
        print()


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} \nПолучился рисунок: \n|||||')
        print()


class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title} \nПолучился рисунок: \n.....')
        print()


object_1 = Pen('Corniva 51')
object_2 = Pencil('ErichKrause')
object_3 = Handle('BIG')
object_1.draw()
object_2.draw()
object_3.draw()
