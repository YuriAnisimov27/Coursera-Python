P, X, Y, K = int(input()), int(input()), int(input()), int(input())
total = X * 100 + Y
i = 1
while i <= K:
    total += int(total * (P / 100))
    i += 1
print(total // 100, total % 100)
