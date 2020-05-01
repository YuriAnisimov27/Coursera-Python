n = int(input())
s = n
counter = 0
while n != 0:
    n = int(input())
    if n > s:
        counter += 1
    s = n
print(counter)
