# 487. Max Consecutive Ones II

from utils import chunk
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # sliding window
        # expand until number of zeroes exceeds 1, then shrink until <= 1
        result = 0
        count = [0, 0]
        i = 0
        for j in range(len(nums)):
            count[nums[j]] += 1
            while i < len(nums) and count[0] > 1:
                count[nums[i]] -= 1
                i += 1
            result = max(result, sum(count))

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 0, 1, 1, 0],
        [1, 0, 1, 0, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findMaxConsecutiveOnes(*puzzle))
