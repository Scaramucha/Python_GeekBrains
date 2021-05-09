def type_logger(function):
    def wrapper(*args):
        for element in args:
            print(f'{element}: {type(element)}')
        return function(*args)
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(4))
