a = list(map(int, input().split()))
b = []
for i in range(1, len(a), 2):
    b.append(a[i])
    b.append(a[i - 1])
if len(a) % 2 != 0:
    b.append(a[-1])
print(*b)
