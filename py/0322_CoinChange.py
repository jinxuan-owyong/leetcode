# 322. Coin Change

from utils import chunk
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        given coins [1,2,5], we need to check using the different possibilities

                      11 
                  /   |   \
                 10   9   6
               / | \
              9  8  5
                /|\
               7 6 3

        make use of a cache to eliminate the duplicate work when starting with 9/6 coins, etc

        for a bottom up approach, let dp[i] be the number of coins we need for amount i
        then if we have amount i and coin c, then we need dp[i-c]+1 coins to make amount i
        """
        # bottom up
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i-coin] + 1
                    )
        return dp[-1] if dp[-1] < float('inf') else -1

        # # top down
        # cache = {}

        # def dfs(remaining):
        #     if remaining in cache:
        #         return cache[remaining]
        #     elif remaining == 0:
        #         return 0

        #     res = float('inf')
        #     for coin in coins:
        #         if coin <= remaining:
        #             curr = dfs(remaining-coin) + 1
        #             if curr < res:
        #                 res = curr

        #     cache[remaining] = res
        #     return res

        # res = dfs(amount)
        # return -1 if res == float('inf') else res


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 5],
        11,
        [2],
        3,
        [1],
        0,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().coinChange(*puzzle))
