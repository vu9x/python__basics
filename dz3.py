def type_logger(func):
    def type_wrapper(*args):
        return_value = func(*args)
        for i in args:
            print(f'{i}: {type(i)}')
        return return_value

    return type_wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
