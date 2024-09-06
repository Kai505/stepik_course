c = ''
x = int(input())
while x != 0:
    if x % 2 == 1:
        c = c + "1"
        x = x // 2
    else:
        c = c + "0"
        x = x // 2
print(c[::-1])
