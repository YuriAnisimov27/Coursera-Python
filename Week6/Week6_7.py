n = int(input())
array = []
for i in range(n):
    array.append(input().split())
    array[i][0], array[i][1] = int(array[i][1]), array[i][0]
array.sort(reverse=True)
for i in range(n):
    print(array[i][1])
