x = int(input())
y = int(input())
a = 0
for i in range(x, y + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        a += 1
print(a)
