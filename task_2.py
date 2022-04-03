class Del:
    def __init__(self, number):
        self.number = number

    def check(self):
        try:
            print(30422 // self.number)
        except ZeroDivisionError:
            print('0 - хорошее число, но попробуйте ввести другое')


operation_1 = Del(1)
operation_1.check()
operation_2 = Del(0)
operation_2.check()
