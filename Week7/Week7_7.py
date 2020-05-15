fin = open('input.txt', 'r', encoding='utf8')
someText = fin.readlines()
words = dict()
for line in someText:
    for i in line.split():
        if i in words:
            words[i] += 1
            print(words[i], end=' ')
        else:
            words[i] = 0
            print(words[i], end=' ')
