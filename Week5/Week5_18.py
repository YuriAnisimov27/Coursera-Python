n = int(input())


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


s = 0
for i in range(1, n + 1):
    s += fact(i)
print(s)
