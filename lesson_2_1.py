arr = [9, "name", 9.5, False, [1, 2, 3]]


def check_type(value):
    return f"Type of item {value} is {type(value)}"


for element in arr:
    print(check_type(element))
