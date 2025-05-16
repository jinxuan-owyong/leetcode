# 494. Target Sum

from typing import List
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        dp[i] is the ways to add/subtract all elements from nums[:i+1]
        then number of ways to reach a sum j is based on the preceding cell(s) that can reach dp[i][j]
        """
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i, n in enumerate(nums):
            for j in list(dp[i].keys()):
                if dp[i][j] > 0:
                    dp[i+1][j+n] += dp[i][j]
                    dp[i+1][j-n] += dp[i][j]
        return dp[-1][target]

# top-down with memoisation
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         seen = {}

#         def knapsack(idx: List[int], total: int):
#             if (idx, total) in seen:
#                 return seen[(idx, total)]

#             if idx == -1:
#                 return 1 if total == target else 0

#             add = knapsack(idx - 1, total + nums[idx])
#             seen[(idx - 1, total + nums[idx])] = add

#             subtract = knapsack(idx - 1, total - nums[idx])
#             seen[(idx - 1, total - nums[idx])] = subtract

#             return add + subtract

#         return knapsack(len(nums) - 1, 0)


if __name__ == "__main__":
    puzzles = [
        ([1, 1, 1, 1, 1], 3),
        ([1], 1),
        ([2], 1),
        [[1, 2, 4, 8, 16], 18293]
    ]
    for puzzle in puzzles:
        print(Solution().findTargetSumWays(*puzzle))
