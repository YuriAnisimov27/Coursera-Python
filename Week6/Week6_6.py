def CountSort(A):
    s = []
    myArray = [0] * 101
    for i in range(101):
        if i in A:
            for j in range(A.count(i)):
                s.append(i)
    for i in range(len(s)):
        A[i] = s[i]


A = list(map(int, input().split()))
CountSort(A)

print(*A)
