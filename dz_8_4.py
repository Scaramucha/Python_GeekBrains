def val_checker(validation):
    def wrapper(function):
        def separation(*args):
            if validation(*args):
                result = function(*args)
                return result
            else:
                raise ValueError(f'Некорректное значение: {args}')
        return separation
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
