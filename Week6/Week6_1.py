def merge(A, B):
    C = []
    i, j = 0, 0
    while i < len(A):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            if j == len(B):
                break
    if j == len(B):
        for k in range(i, len(A)):
            C.append(A[k])
    if i == len(A):
        for k in range(j, len(B)):
            C.append(B[k])

    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
