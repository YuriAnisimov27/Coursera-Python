a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    m = a
elif b >= a and b >= c:
    m = b
elif c >= a and c >= b:
    m = c

if a <= b and a <= c:
    n = a
elif b <= a and b <= c:
    n = b
elif c <= a and c <= b:
    n = c
d = a + b + c - m - n
print(n, d, m)
