from sys import argv


def my_func(h, s, p):
    return h * s + p


print(argv)
h, s, p = [int(i) for i in argv[1:]]
print(my_func(h, s, p))
