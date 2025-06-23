# 31. Next Permutation

from utils import chunk
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        brute force: generate all possible permutations and find the next
        1 2 3 -> 1 3 2
        1 3 2 -> 2 1 3
        2 1 3 -> 2 3 1

        if nums has <= 2 elements, then reverse nums
        starting from the end of nums, find a pivot at index i where nums[i] < nums[i+1]
        then the first number at nums[j] larger than the pivot can be swapped with nums[i]
        sort nums[i+1:] in increasing order to get the result
        - [3,1,2,6,5,4] pivot i = 2, j = 5
        - [3,1,4,6,5,2] swap
        - [3,1,4,2,5,6] sort nums[2+1:] by reversing it
        """

        if len(nums) <= 2:
            nums.reverse()
            return

        # find first increase in adjacent elements
        i = len(nums)-2
        while nums[i] >= nums[i+1]:
            i -= 1

        # the pivot is the largest element, so this is the last permutation
        if i == -1:
            nums.reverse()
            return

        # then find the first number larger than the pivot
        j = len(nums)-1
        while nums[i] >= nums[j]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        # reverse nums[i+1:]
        i, j = i+1, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j-1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
        [2, 3, 1],
    ]
    for puzzle in chunk(puzzles, testSize):
        Solution().nextPermutation(*puzzle)
        print(*puzzle)
