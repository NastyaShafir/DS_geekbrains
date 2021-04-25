my_list = [7, 5, 3, 3, 2]
n = [int(i) for i in input().split()]

for i in n:
    for j in range(len(my_list)):
        if my_list[j] <= i:
            my_list.insert(j, i)
            break
    else:
        my_list.append(i)

print(my_list)