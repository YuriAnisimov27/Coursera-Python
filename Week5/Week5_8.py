a = input().split()
count = 0
index = 0
max = a[0]
for i in a:
    if int(i) >= int(max):
        max = i
        count = index
    index += 1
print(max, count)
