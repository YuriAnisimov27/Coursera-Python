fin = open('input.txt', 'r', encoding='utf8')

class9, class10, class11 = [], [], []
for i in fin:
    line = i.split()
    if int(line[-2]) == 9:
        class9.append(int(line[-1]))
    elif int(line[-2]) == 10:
        class10.append(int(line[-1]))
    elif int(line[-2]) == 11:
        class11.append(int(line[-1]))

print(max(class9), end=' ')
print(max(class10), end=' ')
print(max(class11), end=' ')

fin.close()
