x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + x2 + y1 + y2) % 2 != 0:
    print('NO')
elif y2 > y1 and x1 - (y2 - y1) <= x2 <= x1 + (y2 - y1):
    print('YES')
else:
    print('NO')
