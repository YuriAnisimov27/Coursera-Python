n = int(input())
m = n % 10
if 10 < n < 20 or m == 0:
    print(n, 'korov')
elif 5 <= m <= 9:
    print(n, 'korov')
elif m == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
