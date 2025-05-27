# 153. Find Minimum in Rotated Sorted Array

from utils import chunk
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        index of the smallest integer is the number of rotations
        initially, search range for smallest is [0,len(nums)-1]
        at the rotated point, we will observe a "drop" in the values
        e.g. 6,1,2,3,4,5
        then we will see 2 at the midpoint which is > 1, so search left
        narrow search space to 6,1,2, then mid = 1
        since mid-1 increases, mid is the answer

        if nums[l] > nums[mid], then the drop is somewhere on the left half
        otherwise nums[l] <= nums[mid] and we search right
        """
        res = nums[0]
        i, j = 0, len(nums)-1

        while i <= j:
            # subarray is already sorted, no need to search further
            # take the smallest value
            if nums[i] < nums[j]:
                res = min(res, nums[i])
                break

            mid = i+(j-i)//2
            res = min(res, nums[mid])
            # 6,1,2,3,4,5: mid = 2, search left
            if nums[i] > nums[mid]:
                j = mid - 1
            else:
                i = mid + 1

        return res


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findMin(*puzzle))
