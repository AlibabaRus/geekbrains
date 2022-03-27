class Matrix:
    def __init__(self, mas):
        self.mas = mas

    def __add__(self, other):
        mas_ans = []
        for el1 in range(len(self.mas)):
            mas_add = []
            for el2 in range(len(self.mas[0])):
                mas_add.append(self.mas[el1][el2] + other.mas[el1][el2])
            mas_ans.append(mas_add)
        return Matrix(mas_ans)

    def __str__(self):
        mas_add = ''
        for el1 in range(len(self.mas)):
            for el2 in range(len(self.mas[0])):
                mas_add += str(self.mas[el1][el2]) + ' '
            mas_add += '\n'
        return mas_add


matr_1 = Matrix([[31, 22], [37, 43], [11, 54]])
matr_2 = Matrix([[13, 22], [73, 34], [32, 49]])
print(matr_1 + matr_2)
