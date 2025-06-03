# 152. Maximum Product Subarray

from utils import chunk
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        each time we encounter a negative number, we do not know if 
        there is an odd or even number of negatives ahead
        this can lead to the numbers fluctuating between positive and negative
        during traversal. 
        keep track of the maximum and minimum so far, then if there is a negative,
        it would cause them to swap positions
        O(N) time, O(1) space
        """
        result = nums[0]
        currMin, currMax = 1, 1

        for n in nums:
            lo, hi = currMin, currMax
            currMin = min(n, hi * n, lo * n)
            currMax = max(n, hi * n, lo * n)
            result = max(result, currMax)

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 3, -2, 4],
        [-2, 0, -1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxProduct(*puzzle))
