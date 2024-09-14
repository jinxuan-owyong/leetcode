# 2419. Longest Subarray With Maximum Bitwise AND

from utils import chunk
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # as you perform & operations, a number can only either stay the same or decrease
        # so the longest subarray consists of repeating numbers, or the largest element if unique
        largest = max(nums)
        result = 1
        count = 1
        i, j = 0, 0

        # find the largest subarray that has all max(nums)
        while j < len(nums):
            if nums[i] == largest:
                if j + 1 < len(nums) and nums[j + 1] == nums[i]:
                    count += 1
                    j += 1
                else:
                    result = max(result, count)
                    count = 1
                    i, j = j + 1, j + 1
            else:
                i += 1
                j += 1

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, 3, 2, 2],
        [1, 2, 3, 4],
        [1, 2, 3, 3],
        [1, 1, 2, 3],
        [1, 2, 3, 4, 5, 4, 3, 2, 1],
        [1, 2, 2, 1, 2, 2, 2]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestSubarray(*puzzle))
