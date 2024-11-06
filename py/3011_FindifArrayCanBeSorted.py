# 3011. Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/solutions/6014516/o-n-time-o-1-space-python-one-pass-simple-explanation/

from utils import chunk
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        """
        if array is already sorted, the number of set bits does not matter
        however, subarrays of numbers must have equal number of set bits for successful sorting
        based on the inputs, there is a maximum of 8 bits for any number
        [8,       4,       2       ], [30,      15      ]
         00001000 00000100 00000010    00011110 00001111
        first we attempt to find the largest subarray containing the same number of bits
        then we have arr1, arr2, ...arrN
        we want to ensure that max(arr(i)) < min(arr(i+1)) such that sorting a subarray does not
        result in overlap to the next subarray. if the condition is not fulfilled, then sorting
        is not possible.
        this can be done in 1 pass, by keeping track of the maximum value in the previous subarray
        while we search for the next subarray, each countSetBits operation is O(log(8)), hence 
        giving us O(n * log(8)) = O(n) time and O(1) space complexity
        """

        prevMax, currMin, currMax = -1, float('inf'), -float('inf')
        numBits = nums[0].bit_count()
        bits = numBits
        for n in nums:
            bits = n.bit_count()

            # incoming subarray has different number of bits
            if bits != numBits:
                if prevMax > currMin:
                    return False
                else:
                    prevMax = currMax
                    currMin, currMax = n, n
                    numBits = bits

            # extend current subarray
            currMin = min(n, currMin)
            currMax = max(n, currMax)

        # check last group against the previous subarray
        return prevMax < currMin


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        # TTFFTFT
        [8, 4, 2, 30, 15],
        [1, 2, 3, 4, 5],
        [3, 16, 8, 4, 2],
        [5, 4, 3, 2, 1],
        [1],
        [255, 3],
        [6, 3, 255]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canSortArray(*puzzle))
