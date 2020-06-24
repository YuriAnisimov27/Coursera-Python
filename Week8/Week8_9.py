from itertools import permutations

print('\n'.join(map(''.join, permutations(map(str, range(1, int(input()) + 1))))))

# N = int(input())
# list(map(lambda x: print(*x, sep=''), permutations(range(1, N + 1), N)))
