n = int(input())
maxx = 0
minn = 9
while n != 0:
    last_digit = n % 10
    if last_digit > maxx:
        maxx = last_digit
    if last_digit < minn:
        minn = last_digit
    n = n // 10
print('Максимальная цифра равна', maxx)
print('Минимальная цифра равна', minn)
