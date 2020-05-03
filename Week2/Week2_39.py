n = int(input())
fib, fib1, fib2 = 0, 0, 1
while n > 0:
    fib = fib1 + fib2
    fib2, fib1 = fib1, fib
    n -= 1
print(fib)
