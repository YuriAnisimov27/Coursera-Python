def phib(n):
    return 1 if n == 1 or n == 2 else phib(n - 1) + phib(n - 2)


print(phib(int(input())))
