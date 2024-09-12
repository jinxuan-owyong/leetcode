# 685. Sum of Absolute Differences in a Sorted Array

from utils import chunk
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4, 5]
        # left prefix sum is [1, 3, 6, 10, 15], right prefix sum is [15, 14, 12, 9, 5]
        # then if we want to find the sum absolute difference for 4
        # since nums is non-decreasing, all values before nums[i] yield a non-positive result
        # while all values after nums[i] yield a positive result
        # = | LPS[i - 1] - nums[i] * i | + RPS[i + 1] - nums[i] * (len(nums) - i - 1)
        # = | 6 - 4 * 3 | + 5 - 4 * 1 = 7
        leftPrefix, rightPrefix = [0] * len(nums), [0] * len(nums)
        leftPrefix[0], rightPrefix[-1] = nums[0], nums[-1]

        for i in range(1, len(nums)):
            leftPrefix[i] = leftPrefix[i - 1] + nums[i]

        for i in reversed(range(len(nums) - 1)):
            rightPrefix[i] = rightPrefix[i + 1] + nums[i]

        result = [0] * len(nums)
        total = sum(nums)
        result[0] = total - nums[0] * len(nums)
        result[-1] = abs(total - nums[-1] * len(nums))
        for i in range(1, len(nums) - 1):
            negative = leftPrefix[i - 1] - (nums[i] * i)
            positive = rightPrefix[i + 1] - nums[i] * (len(nums) - i - 1)
            result[i] = abs(negative) + positive

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 3, 5],
        [1, 4, 6, 8, 10],
        [1, 6]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().getSumAbsoluteDifferences(*puzzle))
