n = int(input())
s = 0  # Переменная для суммирования.
# Создаем цикл с итерациями от 1 до n включительно.
for i in range(1, n + 1):
    t = i ** 2  # Возводим i в квадрат и сохраняем результат в переменной t.

    # Проверяем, оканчивается ли квадрат числа t на 2, 5 или 8.
    if t % 10 == 2 or t % 10 == 5 or t % 10 == 8:
        s += i  # Если условие выполняется, добавляем i к сумме s.
# Выводим сумму подходящих чисел.
print(s)
