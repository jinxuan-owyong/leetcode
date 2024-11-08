# 1829. Maximum XOR for Each Query

from utils import chunk
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        [0, 1, 1, 3]
         00 01 01 11
        maximumBit = 2 -> k < 4
        00 ^ 01 ^ 01 ^ 11 ^ k = 11 ^ k
            to maximise 11 ^ k, the ideal value to XOR with would be ~11 = 00, ignoring any leading zeroes
        00 ^ 01 ^ 01 ^ k = 00 ^ k
            similarly k = ~00 = 11 to maximise result
        3rd query is the same as 2nd
        0 ^ k -> k = ~00 = 11

        when performing the bitwise NOT operation, we should take note that k should account
        for any leading 1's resulting from the operation:
            if k is stored as a 32-bit integer
            then ~0b11 = 0b11111111 11111111 11111111 11111100 = -4
            we should mask the resulting output to get a value up to 2**maximumBit - 1
            maximumBit = 2**2 = 4, then mask should be 0b11
        """
        mask = (1 << maximumBit) - 1
        N = len(nums)
        total = 0
        result = [-1] * N

        for i in range(N):
            # we add instead of remove nums[i]
            total ^= nums[i]
            # populate result from back to front instead since XOR is commutative - A^B = B^A
            result[N - 1 - i] = (~total & mask)

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [0, 1, 1, 3],
        2,
        [2, 3, 4, 7],
        3,
        [0, 1, 2, 2, 5, 7],
        3
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().getMaximumXor(*puzzle))
