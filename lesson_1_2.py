t = int(input(" Please enter the time in seconds: "))
h = t % (3600 * 24) // 3600
m = t % (60 * 24) // 60
s = t % 60
print(f"{h:02}:{m:02}:{s:02}")
