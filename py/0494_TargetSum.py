# 494. Target Sum

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        seen = {}

        def knapsack(idx: List[int], total: int):
            if (idx, total) in seen:
                return seen[(idx, total)]

            if idx == -1:
                return 1 if total == target else 0

            add = knapsack(idx - 1, total + nums[idx])
            seen[(idx - 1, total + nums[idx])] = add

            subtract = knapsack(idx - 1, total - nums[idx])
            seen[(idx - 1, total - nums[idx])] = subtract

            return add + subtract

        return knapsack(len(nums) - 1, 0)


if __name__ == "__main__":
    puzzles = [
        ([1, 1, 1, 1, 1], 3),
        ([1], 1),
        ([2], 1),
        [[1, 2, 4, 8, 16], 18293]
    ]
    for puzzle in puzzles:
        print(Solution().findTargetSumWays(*puzzle))

"""
Runtime
266
ms
Beats
13.75%
of users with Python3
Memory
40.60
MB
Beats
13.68%
of users with Python3
17
"""
