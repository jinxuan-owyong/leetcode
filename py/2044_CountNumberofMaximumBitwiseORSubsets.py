# 2044. Count Number of Maximum Bitwise-OR Subsets

from utils import chunk
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        [3,   2,   1,   5   ]
         0011 0010 0001 0101
         maximum bitwise-OR is 0111
        """
        maxOR = 0
        for n in nums:
            maxOR |= n

        cache = {}

        def helper(i: int, currOR: int):
            if i == len(nums):
                # currOR = 0b0111, maxOR = 0b0011
                # using maxOR as a mask tells us if it has all 1 bits from currOR
                return int((currOR & maxOR) == maxOR)
            # recursively include/exclude the current position and memoise
            cache[i] = helper(i + 1, currOR | nums[i]) + helper(i + 1, currOR)
            return cache[i]

        return helper(0, 0)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [3, 1],
        [2, 2, 2],
        [3, 2, 1, 5],
        [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countMaxOrSubsets(*puzzle))
