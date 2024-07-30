# 121. Best Time to Buy and Sell Stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]  # min so far
        profit = 0  # max so far
        for i in range(1, len(prices)):
            currMin = min(currMin, prices[i])
            profit = max(profit, prices[i] - currMin)
        return profit


if __name__ == "__main__":
    puzzles = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [3, 2, 6, 5, 0, 3],
        [3, 3, 1, 3, 3]
    ]
    for puzzle in puzzles:
        print(Solution().maxProfit(puzzle))

"""
Runtime
804
ms
Beats
12.99%
of users with Python3
Memory
27.42
MB
Beats
34.85%
of users with Python3
11
"""
