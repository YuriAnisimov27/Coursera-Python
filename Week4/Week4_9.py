def ReduceFraction(n, m):
    if m == 0:
        return n
    return ReduceFraction(m, n % m)


n = int(input())
m = int(input())

print(n // ReduceFraction(n, m), m // ReduceFraction(n, m))
