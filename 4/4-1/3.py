x = int(input())
a = int(x / 1000)
b = x % 10
c = (x // 10) % 10
n = (x // 100) % 10
if a + b == n - c:
    print("ДА")
else:
    print("НЕТ")
