def my_f(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Нельзя делить на 0"


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(my_f(number1, number2))
