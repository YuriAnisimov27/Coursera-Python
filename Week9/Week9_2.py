from sys import stdin
import copy


class Matrix(list):
    def __init__(self, m):
        self.m = copy.deepcopy(m)

    def __str__(self):
        str_m = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])
        return str_m

    def __add__(self, other):
        m1 = self.m
        m2 = other.m
        return Matrix([list(map(lambda a, b: a + b, m1[i], m2[i]))
                       for i in range(len(m1))])

    def __mul__(self, alpha=0):
        c = copy.deepcopy(self.m)
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                c[i][j] = self.m[i][j] * alpha
        return Matrix(c)

    __rmul__ = __mul__

    def size(self):
        return (len(self.m), len(self.m[0]))


exec(stdin.read())
