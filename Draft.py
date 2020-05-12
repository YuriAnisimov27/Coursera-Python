d = list((set(map(int, input().split()))) & (set(map(int, input().split()))))
d.sort()
print(*d)
