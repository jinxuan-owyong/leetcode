# 1945. Sum of Digits of String After Convert

from utils import chunk


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sumDigits(n: int) -> int:
            result = 0
            while n > 0:
                result += n % 10
                n //= 10
            return result

        BASE = ord('a') - 1
        digits = sum([sumDigits(ord(c) - BASE) for c in s])
        # first sum is performed above
        for _ in range(k - 1):
            digits = sumDigits(digits)
        return digits


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "iiii",
        1,
        "leetcode",
        2,
        "zbax",
        2
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().getLucky(*puzzle))
