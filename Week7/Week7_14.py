N = int(input())
possible = set(range(1, N + 1))
s1 = ''
while s1 != 'HELP':
    s1 = input()
    if s1 != 'HELP':
        now = set([int(s) for s in s1.split()])
        if len(possible & now) * 2 <= len(possible):
            print('NO')
            possible -= now
        else:
            print('YES')
            possible &= now
    else:
        break
print(' '.join(str(i) for i in sorted(possible)))
