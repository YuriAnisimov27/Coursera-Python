from itertools import accumulate
import operator

print(1, *list(accumulate(range(1, int(input()) + 1), operator.mul)))
