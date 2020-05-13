n = int(input())
a = [i for i in range(1, n + 1)]
b = input().split()
c = set(a)
while b[0] != 'HELP':
    answer = input()
    if answer == 'YES':
        c &= set([int(s) for s in b])
    elif answer == 'NO':
        c -= set([int(s) for s in b])
    b = input().split()

print(*sorted(c, key=int))
