# 2270. Number of Ways to Split Array

from utils import chunk
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ways = 0
        left, right = nums[0], sum(nums) - nums[0]
        for i in range(1, len(nums)):
            ways += int(left >= right)
            left += nums[i]
            right -= nums[i]
        return ways


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [10, 4, -8, 7],
        [2, 3, 1, 0]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().waysToSplitArray(*puzzle))
