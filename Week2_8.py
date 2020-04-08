n = int(input())
m = int(input())
k = int(input())
c = (m * n) % k
if (k > m * n) or (k == 1):
    print('NO')
elif (c % m == 0) or (c % n == 0) and (k % m == 0) or (k % n == 0):
    print('YES')
else:
    print('NO')
