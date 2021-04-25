from itertools import count, cycle
from sys import argv


start_number = int(argv[1])
cycle_list = argv[2:]

for el in count(start_number):
    if el > 150:
        break
    else:
        print(el)


с = 0
for el in cycle(cycle_list):
    if с > 10:
        break
    print(el)
    с += 1