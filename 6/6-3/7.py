from math import *

# получаем два числа с плавающей запятой и сохраняем их в переменные 'n' и 'a'
n, a = float(input()), float(input())
# Вычисляем площадь многоугольникам
ans = (n * pow(a, 2)) / (4 * tan(pi / n))
# Выводит результат вычисления площади многоугольника на экран.
print(ans)
