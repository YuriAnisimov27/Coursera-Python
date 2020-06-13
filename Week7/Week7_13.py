n, m = [int(s) for s in input().split()]
a = [int(input()) for i in range(n)]
b = [int(input()) for j in range(m)]

print(len(set(a) & set(b)))
print(*sorted(set(a) & set(b), key=int))

print(len(set(a) - set(b)))
print(*sorted(set(a) - set(b), key=int))

print(len(set(b) - set(a)))
print(*sorted(set(b) - set(a), key=int))
