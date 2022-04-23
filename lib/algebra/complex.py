class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, c):
        return Complex(self.re + c.re, self.im + c.im)

    def __mul__(self, c):
        return Complex(self.re * c.re - self.im * c.im, self.re * c.im + self.im * c.re)

    def __iadd__(self, c):
        self.re += c.re
        self.im += c.im
        return self

    def __imul__(self, c):
        self.re, self.im = self.re * c.re - self.im * c.im, self.re * c.im + self.im * c.re
        return self

    def __repr__(self):
        return f"{self.re} + {self.im}i"
