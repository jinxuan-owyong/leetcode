# 70. Climbing Stairs

from utils import chunk


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        you can only end up at step i if you came from step i-1 or i-2
        so dp[i] = dp[i-1] + dp[i-2]
        """
        first, second = 1, 1
        for _ in range(n-1):
            first, second = second, first + second
        return second


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        1, 2, 3, 4, 5, 6, 7, 8
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().climbStairs(*puzzle))
