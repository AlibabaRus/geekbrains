class Date:
    @classmethod
    def data(cls):
        date = input('Введите дату в формате ДД:ММ:ГГГГ ')
        if cls.valid(date)[0] <= 0 or cls.valid(date)[1] <= 0 or cls.valid(date)[2] <= 0:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] > 12:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 1 and cls.valid(date)[0] > 31:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 2 and cls.valid(date)[0] > 30:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 3 and cls.valid(date)[0] > 31:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 4 and cls.valid(date)[0] > 30:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 5 and cls.valid(date)[0] > 31:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 6 and cls.valid(date)[0] > 30:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 7 and cls.valid(date)[0] > 31:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 8 and cls.valid(date)[0] > 31:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 9 and cls.valid(date)[0] > 30:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 10 and cls.valid(date)[0] > 31:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 11 and cls.valid(date)[0] > 30:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 12 and cls.valid(date)[0] > 31:
            raise ValueError('Вы ввели некоректную дату')
        if cls.valid(date)[1] == 2 and cls.valid(date)[0] > 28 and (
                (cls.valid(date)[2] % 100 == 0 and cls.valid(date)[2] % 400 != 0) or cls.valid(date)[
            2] % 4 != 0):
            raise ValueError('Вы ввели некоректную дату')
        else:
            print("Вы указали коректную дату!")

    @staticmethod
    def valid(date):
        mass = date.split(':')
        if mass[0][0] == 0:
            mass[0] = int(mass[0][1])
        else:
            mass[0] = int(mass[0])
        if mass[1][0] == 0:
            mass[1] = int(mass[1][1])
        else:
            mass[1] = int(mass[1])
        mass[2] = int(mass[2])
        return mass

Date.data()
