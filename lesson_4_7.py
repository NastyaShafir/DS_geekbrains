from sys import argv

n = int(argv[1])


def func(n):
    for i in range(1, n + 1):
        p = 1
        for j in range(1, i + 1):
            p *= j
        yield p


for i in func(n):
    print(i)
