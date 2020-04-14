a = int(input())
count, i = 1, 1
while a != 0:
    a1, a = a, int(input())
    if a1 == a:
        i += 1
        if i > count:
            count = i
    elif a1 != a:
        i = 1
print(count)
