# 136. Single Number

from utils import chunk
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().singleNumber(*puzzle))
