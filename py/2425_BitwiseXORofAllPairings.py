# 2425. Bitwise XOR of All Pairings
#? https://leetcode.com/problems/bitwise-xor-of-all-pairings/solutions/6286933/o-n-time-o-1-space-python3-step-by-step-explanation-with-example/

from utils import chunk
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        suppose we have nums1 = [a1, b1, c1] and nums2 = [a2, b2, c2, d2]
        we want to find (a1^a2 ^ a1^b2 ^ a1^c2 ^ a1^d2) ^ (b1^a2 ^ b1^b2 ^ b1^c2 ^ b1^d2) ^ (c1^a2 ^ c1^b2 ^ c1^c2 ^ c1^d2)
        we know that XOR is associative and commutative
        so the above XOR pairing can be written as
        (a1^a1^a1^a1) ^ (b1^b1^b1^b1) ^ (c1^c1^c1^c1) ^ (a2^a2^a2) ^ (b2^b2^b2) ^ (c2^c2^c2) ^ (d2^d2^d2)
        since XOR of a number itself is 0, and len(nums2) is even, XOR of all elements in nums1 evaluates to 0
        so the expression reduces to
        a2^b2^c2^d2
        observe that
        each of the elements in nums1 is repeated len(nums2) times
        each of the elements in nums2 is repeated len(nums1) times

        if nums1 has even length, then we ignore nums2, since all elements evaluate to 0
        similarly, ignore nums1 if nums2 has even length
        """
        result = 0

        if len(nums1) % 2:
            for n in nums2:
                result ^= n

        if len(nums2) % 2:
            for n in nums1:
                result ^= n

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [2, 1, 3], [10, 2, 5, 0],
        [1, 2], [3, 4]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().xorAllNums(*puzzle))
