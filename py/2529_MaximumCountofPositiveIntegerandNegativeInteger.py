# 2529. Maximum Count of Positive Integer and Negative Integer

from utils import chunk
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        trivial: count and return max
        improved: binary search for the rightmost negative and leftmost positive number to determine its count
        """
        def searchPositiveStart():
            i, j = 0, len(nums)-1
            while i < j:
                mid = i+(j-i)//2
                if nums[mid] <= 0:
                    i = mid + 1
                else:
                    j = mid - 1
            return i if nums[i] > 0 else i + 1

        def searchNegativeEnd():
            i, j = 0, len(nums)-1
            while i < j:
                mid = i+(j-i)//2
                if nums[mid] >= 0:
                    j = mid - 1
                else:
                    i = mid + 1
            return i if nums[i] < 0 else i - 1

        negEnd = searchNegativeEnd()
        posStart = searchPositiveStart()

        countNeg = negEnd + 1 if negEnd >= 0 else 0
        countPos = len(nums)-posStart if posStart < len(nums) else 0

        return max(countNeg, countPos)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [-2, -1, -1, 1, 2, 3],
        [-3, -2, -1, 0, 0, 1, 2],
        [5, 20, 66, 1314],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maximumCount(*puzzle))
