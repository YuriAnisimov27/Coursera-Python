# print(0 == min(map(lambda x: abs(int(x)), open('input.txt').read().split())))
print(not (all(map(int, open('input.txt').read().split()))))
