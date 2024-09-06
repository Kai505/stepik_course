n = int(input())
second = 0
while n > 9:
    second = n % 10
    n = n // 10
print(second)
