s = int(input())
i, a = s, 0
while s != 0:
    s = int(input())
    if s > i:
        a, i = i, s
    elif s > a:
        a = s
print(a)
