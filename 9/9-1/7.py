x = input()
z = 0
for i in range(len(x)):
    if x[i] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        z += 1
    else:
        pass
if z != 0:
    print("Цифра")
else:
    print("Цифр нет")
