# 2226. Maximum Candies Allocated to K Children

from utils import chunk
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        there must be at least as many candies as children
        given x candies per child, each pile can be split among (candies[i]//x) children
        """
        if sum(candies) < k:
            return 0

        i, j = 1, max(candies)

        # use <= instead of < since the extra iteration decrements j for some cases. this happens since we might
        # accidentally overshoot when we set i = mid+1, meaining we assume that all values <= mid are invalid,
        # but might not be the case due to floor division
        while i <= j:
            candiesPerChild = i+(j-i)//2

            # split piles among children
            numChildren = 0
            for pile in candies:
                numChildren += pile // candiesPerChild

            # binary search
            if numChildren >= k:
                i = candiesPerChild+1
            else:
                j = candiesPerChild-1

        return j


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [5, 8, 6],
        3,
        [2, 5],
        11,
        [4, 7, 5],
        3
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maximumCandies(*puzzle))
