total = 1
for i in range(10):
    num = int(input())
    if num > 0 or num < 0:
        total = num * total
print(total)
