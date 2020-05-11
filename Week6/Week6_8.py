fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
K = int(fin.readline())
names = fin.readlines()
points = []
for name in names:
    i = name.split()
    if int(i[-1]) >= 40 and int(i[-2]) >= 40 and int(i[-3]) >= 40:
        points.append((int(i[-1]) + int(i[-2]) + int(i[-3])))

points.sort(reverse=True)
if K >= len(points) or K == 0:
    print(0, file=fout)
elif points[0] == points[K]:
    print(1, file=fout)
elif points[K - 1] == points[K]:
    counter = 0
    while points[K - 1] == points[K - counter]:
        counter += 1
    print(points[K - counter], file=fout)
else:
    print(points[K - 1], file=fout)
fin.close()
fout.close()
