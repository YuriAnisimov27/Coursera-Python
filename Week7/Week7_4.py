fin = open('input.txt', 'r', encoding='utf8')
someText = fin.readlines()
mySet = set()
for words in someText:
    for word in words.split():
        mySet.add(word)

print(len(mySet))

fin.close()
