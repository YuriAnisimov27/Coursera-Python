A, B = int(input()), int(input())
if A < B:
    for i in range(A, B + 1):
        print(i, end=' ')
else:
    for i in range(A, B - 1, -1):
        print(i, end=' ')
