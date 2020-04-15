n = int(input())
i, s = 1, 0
while i <= n:
    s += 1 / (i ** 2)
    i += 1
print(float(s))
