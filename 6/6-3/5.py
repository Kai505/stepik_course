import math

# Получаем число с плавающей запятой и сохраняем его в переменной 'a'
a = float(input())
# Вычисляет округленное в большую сторону значение числа 'a' с помощью функции ceil()
# и округленное в меньшую сторону значение числа 'a' с помощью функции floor().
# Затем складывает эти два значения и выводит результат на экран.
print(math.ceil(a) + math.floor(a))
