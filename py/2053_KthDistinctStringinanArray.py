# 2053. Kth Distinct String in an Array


from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        for s in arr:
            if count[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""


if __name__ == "__main__":
    puzzles = [
        (["d", "b", "c", "b", "c", "a"], 2),
        (["aaa", "aa", "a"], 1),
        (["a", "b", "a"], 3)
    ]
    for puzzle in puzzles:
        print(Solution().kthDistinct(*puzzle))

"""
Runtime
73
ms
Beats
45.89%
Memory
16.90
MB
Beats
7.74%
"""
