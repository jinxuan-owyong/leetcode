# 3254. Find the Power of K-Size Subarrays I

from utils import chunk
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []

        for i in range(len(nums) - k + 1):
            isConsecutiveSorted = True
            j = 0

            while isConsecutiveSorted and j < k - 1:
                isConsecutiveSorted = nums[i + j] + 1 == nums[i + j + 1]
                j += 1

            result.append(max(nums[i:i+k]) if isConsecutiveSorted else -1)

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3, 4, 3, 2, 5],
        3,
        [2, 2, 2, 2, 2],
        4,
        [3, 2, 3, 2, 3, 2],
        2,
        [10, 9, 8, 3, 1, 2],
        2
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().resultsArray(*puzzle))
