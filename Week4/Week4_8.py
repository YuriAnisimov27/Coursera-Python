def pow(a, n):
    if n % 2 != 0:
        if n == 1:
            return a
        return a * pow(a, n - 1)
    elif n % 2 == 0:
        if n == 0:
            return 1
        return pow(a * a, n // 2)


a = float(input())
n = int(input())
print(pow(a, n))
