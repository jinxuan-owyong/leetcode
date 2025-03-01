# 2460. Apply Operations to an Array

from utils import chunk
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 2, 1, 1, 0],
        [0, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().applyOperations(*puzzle))
