class ComplexError(BaseException):
    def __init__(self, complex, other):
        self.first = complex
        self.second = other


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re) + '+' + str(self.im) + 'i'

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re + other.im + self.im * other.re
        elif isinstance(other, int) or isinstance(other, float):
            re = self.re * other
            im = self.im * other
        else:
            error = ComplexError(self, other)
            raise error
        return Complex(re, im)

    __rmul__ = __mul__


a = Complex()
b = Complex(1, 1)
c = Complex(2, 3)
try:
    print('asd' * b)
except ComplexError as ce:
    print('Multiplication error, first param: ', ce.first,
          ' second param: ', ce.second)
