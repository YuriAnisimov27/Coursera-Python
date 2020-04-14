s = int(input())
i, max = 1, s
while s != 0:
    s = int(input())
    if s > max:
        max = s
        i = 1
    elif s == max:
        i += 1
print(i)
