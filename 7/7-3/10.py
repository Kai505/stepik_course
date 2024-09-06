a = 0
for i in range(10):
    x = int(input())
    if x % 2 != 0:
        print("NO")
        break
    a += 1
if a == 10:
    print("YES")
