x = int(input())
y = int(input())
sign = input()
if sign not in ("+", "-", "/", "*"):
    print("Неверная операция")
elif sign == "+":
    print(x + y)
elif sign == "-":
    print(x - y)
elif sign == "*":
    print(x * y)
elif sign == "/" and y == 0:
    print("На ноль делить нельзя!")
else:
    print(x / y)
