n = int(input())
fib, fib1, fib2 = 0, 0, 1
counter = 0
while n >= fib:
    if fib == n:
        print(counter)
        break
    else:
        fib = fib1 + fib2
        fib2, fib1 = fib1, fib
        counter += 1
if fib != n:
    print(-1)