def val_checker(validator):
    def type_logger(func):
        def type_wrapper(*args):
            if validator(*args):
                return_value = func(*args)
                return return_value
            else:
                raise ValueError(f'Wrong val: {args}    ')

        return type_wrapper

    return type_logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)

ab = calc_cube(-5)
print(ab)