a, b, c = str(input()), str(input()), str(input())
x = min(len(a), len(b), len(c))
y = max(len(a), len(b), len(c))
if len(a) == x:
    print(a)
    if len(b) == y:
        print(b)
    else:
        print(c)
elif len(b) == x:
    print(b)
    if len(a) == y:
        print(a)
    else:
        print(c)
elif len(c) == x:
    print(c)
    if len(a) == y:
        print(a)
    else:
        print(b)
