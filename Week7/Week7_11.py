fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
someText = fin.readlines()
words = dict()
counter = 0
for line in someText:
    counter += 1
    if line in words:
        words[line] += 1
    else:
        words[line] = 1
myArray = []
for i in words:
    myArray.append([words[i], i])


def makeTuple(man):
    return (-man[0], man[1])


myArray.sort(key=makeTuple)
if myArray[0][0] > counter / 2:
    print(myArray[0][1].strip(), file=fout)
else:
    print(myArray[0][1].strip(), file=fout)
    print(myArray[1][1].strip(), file=fout)

fin.close()
fout.close()
