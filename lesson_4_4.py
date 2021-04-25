my_list = [int(i) for i in input().split()]
print([i for i in my_list if my_list.count(i) == 1])
