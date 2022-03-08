wage = int(input())
bonus = int(input())
salary = {"wage": wage, "bonus": bonus}


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surnam = surname
        self.position = position
        self._income = salary['wage'] + salary['bonus']


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surnam}')

    def get_total_income(self):
        print(f'{self.position} {self._income}')


worker_1 = Position('Иван', 'Иванов', 'developer')
worker_1.get_full_name()
worker_1.get_total_income()