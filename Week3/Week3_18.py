n = int(input())
x, a = float(input()), float(input())
if n == 0:
    print(a)
else:
    p = a * x
    while n > 1:
        a = float(input())
        p = (p + a) * x
        n -= 1
    print(round(p + float(input()), 6))
