n = int(input())
x = []
for i in range(len(str(n))):
    i = int(str(n)[i])
    if i % 3 == 0:
        x.append(i)
if len(x) == 0:
    print('NO')
else:
    print(max(x))
