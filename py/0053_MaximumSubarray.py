# 53. Maximum Subarray

from utils import chunk
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -float('inf')
        curr = 0
        for i in range(len(nums)):
            # here we are better off starting fresh from nums[i] instead of
            # extending curr since it is already negative, and will not be useful
            if curr < 0:
                curr = nums[i]
            else:
                curr += nums[i]
            best = max(curr, best)
        return best


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxSubArray(*puzzle))
