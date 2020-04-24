def distance(x1, y1, x2, y2):
    A = abs(x1 - x2)
    B = abs(y1 - y2)
    return round((A * A + B * B) ** 0.5, 6)


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(distance(x1, y1, x2, y2))
