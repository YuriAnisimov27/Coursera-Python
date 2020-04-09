a = int(input())
b = int(input())
c = int(input())
k, m = 0, 0
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    k = 1
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    m = 1
if k + m == 2:
    print('YES')
else:
    print('NO')
