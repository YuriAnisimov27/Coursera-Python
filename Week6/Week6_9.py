def Intersection(A, B):
    return set(A) & set(B)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*sorted(Intersection(a, b)))
