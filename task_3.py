class Cell:
    def __init__(self, quantity, row):
        self.quantity = quantity
        self.row = row

    def __add__(self, other):
        return Cell(self.quantity + other, self.row)

    def __sub__(self, other):
        if self.quantity < other:
            return 'Операция невозможна'
        return Cell(self.quantity - other, self.row)

    def __mul__(self, other):
        return Cell(self.quantity * other, self.row)

    def __floordiv__(self, other):
        return Cell(self.quantity // other, self.row)

    def make_order(self):
        return ('*' * self.row + '\n') * (self.quantity // self.row) + '*' * (self.quantity % self.row)


cell_1 = Cell(14, 5)
print(cell_1.make_order())
print('___________')
cell_1 = cell_1 + 2
print(cell_1.make_order())
print('___________')
cell_1 = cell_1 - 3
print(cell_1.make_order())
print('___________')
cell_1 = cell_1 * 2
print(cell_1.make_order())
print('___________')
cell_1 = cell_1 // 3
print(cell_1.make_order())
