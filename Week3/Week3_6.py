p, x, y = int(input()), int(input()), int(input())
n = p * (x * 100 + y) / 100 + (x * 100 + y)
print(int(n // 100), int(n % 100))
