def my_generate_function(number):
    for num in range(number):
        if num % 2 != 0:
            yield num


for_example = my_generate_function(50)
print(next(for_example))
print(next(for_example))
print(next(for_example))
