def get_number():
    month = int(input("Month number: "))
    while month < 1 or month > 12:
        print("Введите корректный номер месяца от 1 до 12")
        month = int(input("Month number: "))
    return month


try:
    month = get_number()
except:
    print("Введите число")
    month = get_number()

arr = [
    ["зима", [1, 2, 12]],
    ["весна", [3, 4, 5]],
    ["лето", [6, 7, 8]],
    ["осень", [9, 10, 11]],
]
for v in arr:
    if month in v[1]:
        print(v[0])
        break

new_dict = {
    "зима": [1, 2, 12],
    "весна": [3, 4, 5],
    "лето": [6, 7, 8],
    "осень": [9, 10, 11],
}
for key in new_dict:
    if month in new_dict[key]:
        print(key)
        break
