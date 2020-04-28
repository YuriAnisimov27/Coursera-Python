a = list(map(int, input().split()))
for i in a:
    if int(i) > 0:
        el = i
for i in a:
    if int(i) > 0 and int(i) < int(el):
        el = i
print(el)
