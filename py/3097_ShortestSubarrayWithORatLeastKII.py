# 3097. Shortest Subarray With OR at Least K II

from utils import chunk
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        identify the set bits in k
        iterate through every window size 1..n to find shortest subarray
        the first window that gives us k is the
        using a sliding window, we increment the count of each bit in the current window 
        until all required bits are in the window
        then we shrink the window until we are below the number of required bits
        repeat growing window until we reach the end
        """
        def enumBits(n: int):
            q = 0
            while n >= (1 << q):
                yield q, 1 if n & (1 << q) else 0
                q += 1

        if k == 0:
            return 1

        curr = 0
        freq = [0] * 32
        result = float('inf')
        i = 0
        for j in range(len(nums)):
            # increment frequencies and set bit in curr if first occurrence
            for b, bit in enumBits(nums[j]):
                freq[b] += bit
                if freq[b] == 1:
                    curr |= 1 << b

            while curr >= k and i < len(nums):
                result = min(j - i + 1, result)
                # decrement frequencies and clear bit in curr if last occurrence
                for b, bit in enumBits(nums[i]):
                    freq[b] -= bit
                    if freq[b] == 0:
                        curr &= ~(1 << b)
                i += 1

        return -1 if result == float('inf') else result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3],
        2,
        [2, 1, 8],
        10,
        [1, 2],
        0
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumSubarrayLength(*puzzle))
