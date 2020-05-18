N = int(input())
myDict = dict()
for i in range(N):
    a, b = input().split()
    myDict[a] = b
    myDict[b] = a

word = input()

print(myDict[word])
