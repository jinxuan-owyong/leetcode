# 238. Product of Array Except Self

from utils import chunk
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        left[i] is the product of all elements from position 0 to position i
        calculate for right as well
        the product of all elements except nums[i] is hence left[i-1] * right[i+1]
        space optimisation: all of the multiplication can be performed on the same array
        """
        left = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i]

        right = [nums[-1]] * len(nums)
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1] * nums[i]

        result = [-1] * len(nums)
        result[0], result[-1] = right[1], left[-2]
        for i in range(1, len(nums)-1):
            result[i] = left[i-1] * right[i+1]

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().productExceptSelf(*puzzle))
