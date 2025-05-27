# 2894. Divisible and Non-divisible Sums Difference

from utils import chunk


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        result = 0
        for i in range(1, n+1):
            if i % m:  # remainder
                result += i  # num1
            else:  # no remainder
                result -= i  # num2
        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        10,
        3,
        5,
        6,
        5,
        1,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().differenceOfSums(*puzzle))
