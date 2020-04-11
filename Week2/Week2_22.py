k, m, n = int(input()), int(input()), int(input())
if n == 0:
    answer = 0
elif k >= n:
    answer = 2 * m
elif k == 1 and n % k == 0:
    answer = n // k * m * 2
elif k == 1 and n % k != 0:
    answer = (n // k + 1) * m * 2
elif (2 * n) % k == 0:
    answer = (2 * n // k) * m
else:
    answer = ((2 * n) // k + 1) * m
print(int(answer))
