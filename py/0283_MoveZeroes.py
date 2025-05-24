# 283. Move Zeroes

from utils import chunk
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        moving all zeroes to the right is the same as moving all non-zero numbers to the left
        if we encounter a non-zero, we swap it with the non-zero pointer to move it in front
        then increment the non-zero pointer to preserve the value
        """
        nonzero = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1
        return nums


# requires O(N + zeroes) time
# count number of zeroes while moving non-zeroes to the front
# then update zeroes from the back at the end
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         zeroes = 0
#         i = 0
#         for j in range(len(nums)):
#             if nums[j] == 0:
#                 zeroes += 1
#             else:
#                 nums[i] = nums[j]
#                 i += 1
#         for j in reversed(range(len(nums)-1, len(nums)-zeroes-1, -1)):
#             nums[j] = 0


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [0, 1, 0, 3, 12],
        [0],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().moveZeroes(*puzzle))
