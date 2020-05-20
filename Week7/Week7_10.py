fin = open('input.txt', 'r', encoding='utf8')
someText = fin.readlines()
words = dict()
for line in someText:
    for i in line.split():
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
myArray = []
for i in words:
    myArray.append([words[i], i])


def makeTuple(man):
    return (-man[0], man[1])


myArray.sort(key=makeTuple)
for i in range(len(myArray)):
    print(myArray[i][1])
