# 875. Koko Eating Bananas

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we know that k is between 1 and max(piles)
        # perform binary search to find k
        # lower k = more time = slower speed since we divide each pile by k
        i, j = 1, max(piles)
        maxTime = j
        while i <= j:
            k = (i + j) // 2
            time = sum([math.ceil(p / k) for p in piles])
            if time <= h:
                maxTime = k  # no need to use max since time < h implies slower
                j = k - 1  # find the slowest time where the criteria is fulfilled
            else:
                i = k + 1
        return maxTime


if __name__ == "__main__":
    puzzles = [
        ([3, 6, 7, 11], 8),
        ([30, 11, 23, 4, 20], 5),
        ([30, 11, 23, 4, 20], 6)
    ]
    for puzzle in puzzles:
        print(Solution().minEatingSpeed(*puzzle))
