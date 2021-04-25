n = int(input("Please enter any positive number:"))
max_digit = 0
while n > 0:
    current_digit = n % 10
    max_digit = max(max_digit, current_digit)
    n //= 10

print(max_digit)
