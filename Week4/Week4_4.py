def MinDivisor(n):
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return i
        else:
            i += 1
    if i <= n ** 0.5:
        return i
    return n


n = int(input())
print(MinDivisor(n))
