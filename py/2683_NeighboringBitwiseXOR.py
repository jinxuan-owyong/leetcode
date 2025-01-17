# 2683. Neighboring Bitwise XOR

from utils import chunk
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        derived[0] = original[0] ^ original[1] = 0 ^ 1 = 1 
        derived[1] = original[1] ^ original[2] = 1 ^ 0 = 1
        derived[2] = original[2] ^ original[0] = 0 ^ 0 = 0

        derived[0] ^ derived[1] ^ derived[2] ... 
        = original[0] ^ original[1] ^ original[1] ^ original[2] ^ original[2] ^ original[0]
        = 0 (since x^x = 0)

        we know if the array is not valid if the XOR of all elements of derived is not 0
        """
        result = 0
        for n in derived:
            result ^= n
        return result == 0


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 1, 0],
        [1, 1],
        [1, 0]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().doesValidArrayExist(*puzzle))
