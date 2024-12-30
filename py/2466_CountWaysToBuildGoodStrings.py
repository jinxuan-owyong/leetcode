# 2466. Count Ways To Build Good Strings

from utils import chunk


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1E9 + 7
        # number of good strings for each size
        dp = [0] * (high + 1)
        dp[0] = 1  # from empty string, 1 as the base counter

        for i in range(1, high+1):
            # from the previous string, we append ('0')*zero or ('1')*one
            # dp[prev] times respectively, giving us a new dp[i] combinations
            # (0001, 1000, 1111) -> (zero = 3, one = 1) -> 3 + 3
            if (prev := i - zero) >= 0:
                dp[i] += dp[prev]
            if (prev := i - one) >= 0:
                dp[i] += dp[prev]
            dp[i] %= MOD

        return int(sum(dp[low:high+1]) % MOD)

        # MOD = 1E9 + 7
        # cache = {}
        # def dfs(size: int):
        #     if size in cache:
        #         return cache[size]

        #     if size > high:
        #         return 0

        #     count = 0

        #     # include the string itself
        #     count += int(size >= low and size <= high)
        #     # and potential future strings when appending '0's or '1's
        #     count += dfs(size + zero)
        #     count += dfs(size + one)

        #     cache[size] = int(count % MOD)
        #     return cache[size]
        # return int(dfs(0) % MOD)


if __name__ == "__main__":
    testSize = 4
    puzzles = [
        3, 3, 1, 1,
        2, 3, 1, 2,
        1, 900, 1, 1,
        1, 100000, 1, 1

    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countGoodStrings(*puzzle))
