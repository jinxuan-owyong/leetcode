# 2401. Longest Nice Subarray

from utils import chunk
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        if A & B == 0, then there are no duplicate set bits
        e.g. 0011 & 1000 = 0000 (3 & 8)
        => a window is valid if all elements have no common set bit
        => window can be expanded if window & nums[j] == 0
        => otherwise shrink window until condition is valid
        """
        result = 1
        window = 0  # bitmask
        i = 0

        for j in range(len(nums)):
            # ensure adding nums[j] will result in a valid window, shrinking if necessary
            while i < j and window & nums[j] > 0:
                window ^= nums[i]
                i += 1
            if (window & nums[j]) == 0:
                window ^= nums[j]
                result = max(result, j-i+1)

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 3, 8, 48, 10],
        [3, 1, 5, 11, 13],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestNiceSubarray(*puzzle))
