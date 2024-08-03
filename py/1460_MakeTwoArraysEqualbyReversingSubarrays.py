# 1460. Make Two Arrays Equal by Reversing Subarrays


from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


if __name__ == "__main__":
    puzzles = [
        ([1, 2, 3, 4], [2, 4, 1, 3]),
        ([7], [7]),
        ([3, 7, 9], [3, 7, 11])
    ]
    for puzzle in puzzles:
        print(Solution().canBeEqual(*puzzle))

"""
Runtime
79
ms
Beats
28.57%
Analyze Complexity
Memory
16.86
MB
Beats
22.18%
"""
