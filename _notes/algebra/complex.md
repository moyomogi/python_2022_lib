---
layout: page
title: algebra/complex
---

# algebra/complex

[View on GitHub](https://github.com/moyomogi/python_2022_lib/blob/master/lib/algebra/complex.py)

複素数の計算を行う関数です。計算量はいずれのメソッドも $O(1)$ です。

```py
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
```

## リンク
- [[algebra/calc_rect_area]]
- [[algebra/complex]]
- [[data_structures/dsu]]
