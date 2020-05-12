a = list(map(int, input().split()))
mySet = set()
for element in a:
    if element in mySet:
        print('YES')
    else:
        print('NO')
    mySet.add(element)
