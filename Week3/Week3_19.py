s, sum = 0, 0
x = int(input())
n = 0
while x != 0:
    n += 1
    s += x
    sum += x ** 2
    x = int(input())
a = ((sum - s ** 2 / n) / (n - 1)) ** 0.5
print(a)
