x = input()
c = 0
for i in range(len(x) - 1):
    if x[i] == x[i + 1]:
        c += 1
print(c)
