A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
if A1 >= B1 and A1 >= C1:
    H1 = A1
elif B1 >= A1 and B1 >= C1:
    H1 = B1
else:
    H1 = C1

if A1 <= B1 and A1 <= C1:
    M1 = A1
elif B1 <= A1 and B1 <= C1:
    M1 = B1
else:
    M1 = C1

L1 = A1 + B1 + C1 - M1 - H1

if A2 >= B2 and A2 >= C2:
    H2 = A2
elif B2 >= A2 and B2 >= C2:
    H2 = B2
else:
    H2 = C2

if A2 <= B2 and A2 <= C2:
    M2 = A2
elif B2 <= A2 and B2 <= C2:
    M2 = B2
else:
    M2 = C2

L2 = A2 + B2 + C2 - M2 - H2

if H1 == H2 and L1 == L2 and M1 == M2:
    print('Boxes are equal')
elif H1 >= H2 and L1 >= L2 and M1 >= M2:
    print('The first box is larger than the second one')
elif H2 >= H1 and L2 >= L1 and M2 >= M1:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
