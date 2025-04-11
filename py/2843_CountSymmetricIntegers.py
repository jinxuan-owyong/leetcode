# 2843. Count Symmetric Integers

from utils import chunk
import math


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # high <= 10^4 so half of digits < 100
        # pre-calculate all integer sums, and compare their left and right
        sumDigits = [sum(int(c) for c in str(n)) for n in range(100)]
        result = 0

        i = low
        while i <= high:
            # note: math.log(1000, 10) < math.log10(1000)
            # https://stackoverflow.com/a/14577413/19182765
            digits = math.floor(math.log10(i))+1
            if digits % 2 == 0:
                left, right = i // 10**(digits//2), i % 10**(digits//2)
                result += int(sumDigits[left] == sumDigits[right])
                i += 1
            else:
                # odd digits are never symmetric
                # round to the next nearest place e.g. if low = 123 -> next valid is 1000
                i = 10**digits

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        1, 100,
        1200, 1230,
        123, 1001,
        2, 11

    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countSymmetricIntegers(*puzzle))
