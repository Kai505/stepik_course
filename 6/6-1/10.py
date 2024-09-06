x = int(input())
a = x // 100 % 10
b = x % 10
c = x // 10 % 10
if max(a, b, c) - min(a, b, c) == (a + b + c) - min(a, b, c) - max(a, b, c):
    print("Число интересное")
else:
    print("Число неинтересное")
