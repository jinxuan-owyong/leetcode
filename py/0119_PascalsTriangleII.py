# 119. Pascal's Triangle II

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        seenFact = {}
        seenNCR = {}
        seenFact[0] = 1

        def factorial(n: int) -> int:
            if n in seenFact:
                return seenFact[n]
            seenFact[n] = n * factorial(n - 1)
            return seenFact[n]

        def nCr(n: int, r: int):
            if (n,  n - r) in seenNCR:
                return seenNCR[(n, n - r)]
            seenNCR[(n, r)] = int(factorial(n) /
                                  (factorial(r) * factorial(n - r)))
            return seenNCR[(n, r)]

        return [nCr(rowIndex, i) for i in range(rowIndex + 1)]


if __name__ == "__main__":
    puzzles = [0, 1, 2, 3, 4, 5]
    for puzzle in puzzles:
        print(Solution().getRow(puzzle))

"""
Runtime
31
ms
Beats
80.83%
of users with Python3
Memory
16.55
MB
Beats
36.71%
of users with Python3
3
"""
