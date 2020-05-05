a = list(map(int, input().split()))
b = []
for i in range(a[1]):
    b.append(int(input()))
b.sort()
sum = 0
for i in range(len(b)):
    sum += b[i]
    if sum == a[0]:
        print(i + 1)
        break
    if sum > a[0]:
        print(i)
        break
if sum < a[0]:
    print(len(b))
