n = int(input())
# Проходим по числам от 1 до n включительно
for i in range(1, n + 1):
    # Проверяем, принадлежит ли i одному из диапазонов (5-9, 17-37, 78-87)
    if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
        continue  # Если i находится в одном из диапазонов, переходим к следующей итерации цикла
    print(i)
