from math import *

# Поскольку тригонометрические функции работают с радианами, нужно градусы перевести в радианы
x = radians(float(input()))
res = sin(x) + cos(x) + tan(x) ** 2
print(res)
