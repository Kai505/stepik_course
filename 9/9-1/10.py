x = input()
x = x.lower()
a = 0
d = 0
glass = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
soglass = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
for i in range(0, len(x)):
    if x[i] in glass:
        a += 1
    elif x[i] in soglass:
        d += 1
print(f"Количество гласных букв равно {a}")
print(f"Количество согласных букв равно {d}")
