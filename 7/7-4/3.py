x = ""
y = 0
while x != "стоп" or x != "хватит" or x != "достаточно":
    x = input()
    if x == "стоп" or x == "хватит" or x == "достаточно":
        break
    else:
        y += 1
print(y)
