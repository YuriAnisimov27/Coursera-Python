a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print(3)
elif a == 0 and b == 0:
    print(0)
elif a == 0 and b != 0:
    print(1, -c / b)
elif d == 0:
    x = (-b + d ** 0.5) / (2 * a)
    print(1, float(x))
elif d > 0:
    x1 = float((-b + d ** 0.5) / (2 * a))
    x2 = float((-b - d ** 0.5) / (2 * a))
    if x1 < x2:
        print(2, x1, x2)
    else:
        print(2, x2, x1)
elif d < 0:
    print(0)
