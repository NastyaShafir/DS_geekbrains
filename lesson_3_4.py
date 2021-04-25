def my_func(x, y):
    result = 1
    for i in range(-y):
        result *= x
    return 1 / result


print(my_func(2, -3))
