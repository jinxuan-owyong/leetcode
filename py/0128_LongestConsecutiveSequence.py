# 128. Longest Consecutive Sequence

from utils import chunk
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        trivial: sort the array and scan
        using a hash set, n is a valid start value iff n-1 does not exist in the set
         -> this is always true if n is a non-start value
        if valid start value, then scan the array for consecutive size
        """
        longest = 0
        values = set(nums)
        checked = set()

        for n in nums:
            if n-1 not in values and n not in checked:
                checked.add(n)
                count = 0
                while n in values:
                    count += 1
                    n += 1
                if count > longest:
                    longest = count

        return longest


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestConsecutive(*puzzle))
