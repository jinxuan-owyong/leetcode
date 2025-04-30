# 1295. Find Numbers with Even Number of Digits

from utils import chunk
from typing import List
import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            digits = 1
            while math.pow(10, digits) <= n:
                digits += 1
            result += int(digits % 2 == 0)
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [12, 345, 2, 6, 7896],
        [555, 901, 482, 1771],
        [1000],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findNumbers(*puzzle))
