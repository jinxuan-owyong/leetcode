# 33. Search in Rotated Sorted Array

from utils import chunk
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1

        while i <= j:
            mid = i+(j-i)//2
            if nums[mid] == target:
                return mid

            # either half of the array is sorted (extreme left < extreme right)
            # note: <= is used here since i can be equal to mid
            # e.g. in [3,1], we want to search right for target = 1
            if nums[i] <= nums[mid]:
                # check if target is contained in the left half
                if nums[i] <= target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                # similarly, check if target is in right half
                if nums[mid] < target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1

        return -1


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [4, 5, 6, 7, 0, 1, 2],
        0,
        [4, 5, 6, 7, 0, 1, 2],
        3,
        [1],
        0,
        [3, 1],
        1,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().search(*puzzle))
