a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == 0:
    y = e / b
    x = (f - d * y) / c
else:
    y = float((f - c * e / a) / (d - c * b / a))
    x = float((e - b * y) / a)
print(x, y)
