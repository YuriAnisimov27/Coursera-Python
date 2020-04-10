A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())

a, b, c = int(A1 / A2), int(B1 / C2), int(C1 / B2)
n1 = a * b * c
a, b, c = int(A1 / A2), int(B1 / B2), int(C1 / C2)
n2 = a * b * c
a, b, c = int(A1 / B2), int(B1 / A2), int(C1 / C2)
n3 = a * b * c
a, b, c = int(A1 / B2), int(B1 / C2), int(C1 / A2)
n4 = a * b * c
a, b, c = int(A1 / C2), int(B1 / A2), int(C1 / B2)
n5 = a * b * c
a, b, c = int(A1 / C2), int(B1 / B2), int(C1 / A2)
n6 = a * b * c

count = max(n1, n2, n3, n4, n5, n6)

print(count)
