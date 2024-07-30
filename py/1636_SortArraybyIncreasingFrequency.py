# 1636. Sort Array by Increasing Frequency

from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Counter returns (num, freq)[]
        count = sorted(Counter(nums).items(), key=lambda x: (x[1], -1 * x[0]))
        result = []
        for num, freq in count:
            result.extend([num] * freq)
        return result


if __name__ == "__main__":
    puzzles = [
        [1, 1, 2, 2, 2, 3],
        [2, 3, 1, 3, 2],
        [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    ]
    for puzzle in puzzles:
        print(Solution().frequencySort(puzzle))

"""
Runtime
51
ms
Beats
49.72%
Memory
16.66
MB
Beats
12.04%
"""
