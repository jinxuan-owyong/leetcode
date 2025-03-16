# 3487. Maximum Unique Subarray Sum After Deletion

from utils import chunk
from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        since we can delete any number of elements, it is equivalent to
        picking any subsequence from nums before deletion
        we only want to pick positive integers
        """
        added = set()
        result = 0

        for n in nums:
            if n > 0 and n not in added:
                result += n
                added.add(n)

        # use max as fallback if nums[i] <= 0 for all i
        return result if result > 0 else max(nums)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, 4, 5],
        [1, 1, 0, 1, 1],
        [1, 2, -1, -2, 1, 0, -1],
        [-1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxSum(*puzzle))
