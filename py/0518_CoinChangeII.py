# 518. Coin Change II

from utils import chunk
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom-up
        # dp[c] is the combinations that can be formed with all coins at and after coin c
        # coins[i] = c
        # then dp[i][a] is the number of combinations for amount a
        # number of combinations at dp[i][a] is sum (if possible) of
        # - same amount, but all coins after c: dp[i+1][a],
        # - same coin, but building upon the previous amount a-c: dp[i][a-c]

        # O(amount) space
        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(len(coins)):  # forwards and backwards both work
            c = coins[i]
            for a in range(1, amount+1):
                # since we are always performing dp[i][a] += dp[i+1][a]
                # the value of a column only increases when there is an adjacent cell that we can extend from
                # hence we do not have to duplicate the data and instead build upon the previous values
                dp[a] += dp[a-c] if a-c >= 0 else 0

        return dp[-1]

        # O(amount * coins) space
        # dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        # for i in range(len(coins)):
        #     dp[i][0] = 1 # only 1 way to form amount of 0 regardless of number of coins

        # # start with 1 coin (the last), then introduce more coins
        # for i in reversed(range(len(coins))):
        #     c = coins[i]
        #     for a in range(1, amount+1):
        #         dp[i][a] += dp[i+1][a]
        #         if a-c >= 0:
        #             dp[i][a] += dp[i][a-c]

        # return dp[0][-1]

        # # brute force memoisation
        # cache = {}

        # # uses O(amount * len(coins)) space since we have to cache every combination
        # def helper(curr, i):
        #     if (k := (curr, i)) in cache:
        #         return cache[k]
        #     elif curr == amount:
        #         return 1
        #     elif curr > amount or i == len(coins):
        #         return 0

        #     # we only want to take an equal or larger value coin
        #     # to avoid 1,2,1 and 2,1,1 permutations
        #     # so we keep track of the lowest index allowed using i
        #     result = helper(curr + coins[i], i) + helper(curr, i+1)

        #     cache[(curr, i)] = result
        #     return result

        # return helper(0, 0)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        5,
        [1, 2, 5],
        3,
        [2],
        10,
        [10],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().change(*puzzle))
