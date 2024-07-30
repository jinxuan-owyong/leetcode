# 1929. Concatenation of Array

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


if __name__ == "__main__":
    puzzles = [
        [1, 2, 1],
        [1, 3, 2, 1]
    ]
    for puzzle in puzzles:
        print(Solution().getConcatenation(puzzle))

"""
Runtime
70
ms
Beats
57.31%
Memory
16.80
MB
Beats
82.18%
"""
