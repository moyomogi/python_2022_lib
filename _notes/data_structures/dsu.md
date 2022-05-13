---
layout: page
title: data_structures/dsu
---

# data_structures/dsu

[View on GitHub](https://github.com/moyomogi/python_2022_lib/blob/master/lib/data_structures/dsu.py)

集合を扱うデータ構造。
- `merge(a, b)`: 要素 `a` の属する集合と要素 `b` の属する集合を併合する。
- `same(a, b)`: 要素 `a`, `b` が同じ集合に属するかを返す。
- `find(a)`: 要素 `a` が属する集合の根を返す。
- `size(a)`: 要素 `a` が属する集合の要素数を返す。
- `groups()`: 現在の集合の状態を表したリストを返す。

```py
# https://github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
import typing


class DSU:
    '''
    Implement (union by size) + (path halving)
    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))
```

## リンク
- [[algebra/calc_rect_area]]
- [[algebra/complex]]
- [[data_structures/dsu]]
