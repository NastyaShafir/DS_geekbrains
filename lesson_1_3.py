n = input("Please enter any number: ")

while int(n) < 0:
    # print("Sorry! It is wrong number.")
    n = input("Please enter any number greater '0':")

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
