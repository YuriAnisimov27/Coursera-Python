a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    h, k, l = a, b, c
elif b > a and b > c:
    h, k, l = b, a, c
else:
    h, k, l = c, a, b
x = k ** 2 + l ** 2
if h < k + l:
    if h ** 2 > x:
        print('obtuse')
    if h ** 2 < x:
        print('acute')
    if h ** 2 == x:
        print('rectangular')
else:
    print('impossible')
