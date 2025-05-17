# 75. Sort Colors

from utils import chunk
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        i = 0
        for colour, freq in enumerate(count):
            for _ in range(freq):
                nums[i] = colour
                i += 1
        return nums


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().sortColors(*puzzle))
