# 50. Pow(x, n)

from utils import chunk


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # since x^n * x^n = x^(2n)
            # recursively call helper to calculate in O(log n) time
            if n == 0:
                return 1
            half = helper(x, n // 2)
            result = half * half
            # odd number of powers is not calculated in half
            if n % 2 == 1:
                result *= x
            return result

        # convert base into positive value
        # 2^-2 = (1/2)^2
        if n < 0:
            x = 1 / x
            n = -n

        return helper(x, n)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        2.00000, 10,
        2.10000, 3,
        2.00000, -2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().myPow(*puzzle))
