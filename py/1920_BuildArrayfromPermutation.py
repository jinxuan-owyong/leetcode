# 1920. Build Array from Permutation

from utils import chunk
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        make use of the 0-bits in a 32-bit number to store the result
        since 1 <= nums[i] <= 1000, only the right 10 bits are used
        use the 11th-20th bits to store nums[nums[i]] in the first pass
        then right shift by 10 bits in the second pass
        0x3FF = 0b11_1111_1111
        """
        for i in range(len(nums)):
            nums[i] |= (nums[nums[i] & 0x3FF] & 0x3FF) << 10
        for i in range(len(nums)):
            nums[i] >>= 10
        return nums


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [0, 2, 1, 5, 3, 4],
        [5, 0, 1, 2, 3, 4]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().buildArray(*puzzle))
