# 213. House Robber II

from utils import chunk
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # if we rob the first house, we cannot rob the last house
        # otherwise we do not rob adjacent houses
        # pretend the last/first house doesn't exist if we rob the first/last house
        # then take the better of 2 results

        if len(nums) <= 2:
            return max(nums)

        def rob2(i: int, j: int) -> int:
            # same as the first problem
            a, b = 0, 0
            for k in range(i, j+1):
                a, b = b, max(a+nums[k], b)
            return b

        return max(rob2(0, len(nums)-2), rob2(1, len(nums)-1))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [1, 2, 3],
        [1],
        [1, 2],
        [2, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().rob(*puzzle))
