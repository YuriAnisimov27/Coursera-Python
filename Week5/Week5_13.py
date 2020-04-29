a = list(map(int, input().split()))
b = []
for i in a:
    if i == min(a):
        b.append(max(a))
    elif i == max(a):
        b.append(min(a))
    else:
        b.append(i)
print(*b)
