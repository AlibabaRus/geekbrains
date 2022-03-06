def type_logger(f):
    def types(*args):
        result = f(*args)
        print(result)
        return type(*args)
    return types


@type_logger
def calc_cube(x):
   return x ** 3
print(calc_cube(int(input())))