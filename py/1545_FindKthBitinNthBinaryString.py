# 1545. Find Kth Bit in Nth Binary String

from utils import chunk


class Solution:
    # recursion
    def findKthBit(self, n: int, k: int) -> str:
        # length of S is
        # S1 = 1
        # S2 = 3
        # S3 = 7
        # S4 = 15
        # Si = 2^i - 1
        # if k <= length // 2     -> it is equal to findKthBit(n - 1, k)
        # if k == length // 2 + 1 -> 1 since we always add "1" in the middle
        # otherwise               -> flip(findKthBit(n - 1, len(n) - k + 1))

        # 011100110110001
        # 0:14 > 0:6 = flip(reversed(8:14))
        # n = 4, k = 9 -> flip(findKthBit(3, 6))

        if n == 1:
            return "0"

        bits = 2**n - 1
        if k <= bits // 2:
            return self.findKthBit(n - 1, k)
        elif k == bits // 2 + 1:
            return "1"
        else:
            result = self.findKthBit(n - 1, bits - k + 1)
            return "1" if result == "0" else "0"


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        3, 1,
        4, 11,
        1, 1,
        3, 2,
        20, 1234
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findKthBit(*puzzle))

# class Solution:
#     # brute force
#     def findKthBit(self, n: int, k: int) -> str:
#         s = "0"

#         while n:
#             s = s + "1" + "".join(reversed(["1" if c == "0" else "0" for c in s]))
#             n -= 1

#         return s[k - 1]
