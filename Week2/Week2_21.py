a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == 0 and b == 0:
    print('INF')
elif a == 0 and b != 0:
    print('NO')
elif (c * (-b / a) + d) == 0:
    print('NO')
elif -b // a != -b / a:
    print('NO')
elif a != 0:
    print(-b // a)
else:
    print('NO')
