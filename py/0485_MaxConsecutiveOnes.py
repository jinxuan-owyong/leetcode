# 485. Max Consecutive Ones

from utils import chunk
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for n in nums:
            count += n
            result = max(result, count)
            if n == 0:
                count = 0
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findMaxConsecutiveOnes(*puzzle))
