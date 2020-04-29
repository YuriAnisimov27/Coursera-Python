N = int(input())
a = list(map(int, input().split()))
x = int(input())
if N == 1:
    print(*a)
else:
    x1, x2 = x, x
    count = a.count(x)
    while count == 0:
        x1 += 1
        x2 -= 1
        count = a.count(x1) + a.count(x2)
    if a.count(x1) != 0:
        print(x1)
    else:
        print(x2)
