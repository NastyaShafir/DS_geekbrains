def my_func():
    s = input()
    s2 = 0
    while s != "#":
        numbers = s.split()  # ['1', '2', '3']
        for i in numbers:
            if i != "#":
                s2 += int(i)
            else:
                print(s2)
                return
        print(s2)
        s = input()


my_func()