x = int(input())
y = int(input())
if y % (y - x + 1) == 0 or y == 1:
    print('YES')
else:
    print('NO')
