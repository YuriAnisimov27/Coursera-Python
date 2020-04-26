def IsPointInSquare(x, y):
    return (-1 <= abs(x) + abs(y) <= 1)


x, y = float(input()), float(input())
IsPointInSquare(x, y)
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
