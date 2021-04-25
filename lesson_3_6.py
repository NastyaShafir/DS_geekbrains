def int_func(text: str):
    return chr(ord(text[0]) - 32) + text[1:]


print(int_func("text"))

words = input().split()
print(" ".join(list(map(int_func, words))))
