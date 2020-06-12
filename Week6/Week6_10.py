size = int(input())
shoes = list(map(int, input().split()))
counter = 0
for shoe in sorted(shoes):
    if shoe >= size:
        size = shoe + 3
        counter += 1
print(counter)
