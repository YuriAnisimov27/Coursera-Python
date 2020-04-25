def distance(x1, y1, x2, y2):
    A = abs(x1 - x2)
    B = abs(y1 - y2)
    return round((A * A + B * B) ** 0.5, 6)


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
a = distance(x1, y1, x2, y2)
b = distance(x3, y3, x2, y2)
c = distance(x1, y1, x3, y3)
p = (a + b + c)
print(round(p, 6))
