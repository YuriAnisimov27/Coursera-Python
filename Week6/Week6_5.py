fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

names = fin.readlines()
names.sort()
for name in names:
    i = name.split()
    print(i[0], i[1], i[3], file=fout, sep=' ')

fin.close()
fout.close()
