def IsPrime(n):
    i = int(n ** 0.5)
    while i > 1:
        if n % i == 0:
            break
        else:
            i -= 1
    return i == 1


n = int(input())

if IsPrime(n):
    print('YES')
else:
    print('NO')
