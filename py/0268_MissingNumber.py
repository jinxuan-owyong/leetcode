# 268. Missing Number

from utils import chunk
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        using the XOR operator, we can check for a missing value pairs
        since there are n integers in nums, they can paired 1-1 to [0,n]
        except the missing number
        """
        check = len(nums)  # n
        for i in range(len(nums)):
            check ^= i  # [0,n-1]
            check ^= nums[i]
        return check

        # # sorting with constant space
        # nums.sort()
        # if nums[0] != 0:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i]+1 != nums[i+1]:
        #         return nums[i]+1
        # return nums[-1]+1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().missingNumber(*puzzle))
