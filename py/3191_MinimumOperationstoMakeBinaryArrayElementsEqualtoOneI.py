# 3191. Minimum Operations to Make Binary Array Elements Equal to One I

from utils import chunk
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        # flip the next 3 elements nums[j:j+3]
        for j in range(len(nums)-2):
            if nums[j] == 0:
                flips += 1
                nums[j], nums[j+1], nums[j+2] = 1 - \
                    nums[j], 1-nums[j+1], 1-nums[j+2]

        # last 3 elements should all be ones
        if all(map(lambda x: x == 1, nums[-3:])):
            return flips
        else:
            return -1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minOperations(*puzzle))
