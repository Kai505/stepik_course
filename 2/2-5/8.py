abc = int(input())
c = abc % 10  # Последняя цифра числа
b = (abc % 100) // 10  # Предпоследняя цифра числа
a = abc // 100  # Первая цифра числа
# Выводим перебор всех перестановок цифр
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
