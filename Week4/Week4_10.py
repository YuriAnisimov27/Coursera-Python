def sumNumbers():
    n = int(input())
    if n == 0:
        return 0
    return sumNumbers() + n


print(sumNumbers())
