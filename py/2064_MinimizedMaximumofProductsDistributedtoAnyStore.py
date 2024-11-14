# 2064. Minimized Maximum of Products Distributed to Any Store

from utils import chunk
from typing import List
import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        """
        intuition: assume there is only 1 store
        using binary search, we can determine 0 < k <= q such that
        q = m * k + (n - m) * (k + 1)
        11 -> 2, 3, 3, 3
        then the desired maximum is k + 1 = 3
        k fulfills the following criteria:
        k * n <= q < (k + 1) * n

        to expand this idea to n stores
        we know that 1 <= k <= max(quantities)
        we try to find the minimum value of x such that we can distribute all quantities
        given q[i], it we need to distribute to ceil(q[i] / x) stores
        then check if the sum of stores required matches n
        """
        i, j = 1, max(quantities)
        result = float('inf')

        while i <= j:
            x = (i + j) // 2
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
            if stores <= n:
                # every new value of x here will be smaller than the previous, no min() required
                result = x
                j = x - 1
            else:
                i = x + 1

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        6, [11, 6],
        7, [15, 10, 10],
        1, [100000],
        4, [9]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimizedMaximum(*puzzle))
