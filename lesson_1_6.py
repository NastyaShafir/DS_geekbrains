# a = float(input("Please enter your start point: "))
# b = float(input("Please enter your finish point: "))
# days = 1
# while a < b:
#     a *= 1.1
#     days += 1
# print(f"You run for {days} days more than {int(b)} km")

# a = float(input())
# b = float(input())


# def km(a, days, b):
#     if a >= b:
#         return days
#     else:
#         return km(a * 1.1, days + 1, b)


# print(km(a, 1, b))
def km(a, days, b):
    if a >= b:
        return days
    else:
        return km(a * 1.1, days + 1, b)

a = float(input())
b = float(input())

if a >= b || b == 0 || a < 0 || b < 0:
  print('Введите корректные данные')
  exit()

print(km(a, 1, b))
