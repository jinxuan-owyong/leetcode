# 746. Min Cost Climbing Stairs

from utils import chunk
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up
        # dp[i] is the cost to reach the end starting from stair i
        # we can reach stair i from stair i-1 or stair i-2
        if len(cost) == 1:
            return cost[0]

        dp = [0] * (len(cost)+2)
        for i in reversed(range(len(cost))):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[:2])  # you can start take 2 steps from before index 0

        # # top-down
        # cache = {}
        # def recursion(i):
        #     if i in cache:
        #         return cache[i]
        #     if i == len(cost):
        #         return 0
        #     if i > len(cost):
        #         return float('inf')
        #     cache[i] = cost[i] + min(
        #         recursion(i+1),
        #         recursion(i+2)
        #     )
        #     return cache[i]
        # return min(
        #     recursion(0),
        #     recursion(1)  # you can start take 2 steps from before index 0
        # )


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [10, 15, 20],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minCostClimbingStairs(*puzzle))
