K = int(input())
counter = 0
while K:
    if K == int(str(K)[::-1]):
        counter += 1
    K -= 1
print(counter)
