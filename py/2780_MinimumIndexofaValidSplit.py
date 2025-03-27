# 2780. Minimum Index of a Valid Split

from utils import chunk
from typing import List
from collections import defaultdict


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        identify the dominant element x using a hashmap
        find the prefix sum of the freqeuency of x, in array prefix[i:j+1]
        check through nums in O(n) time to know whether nums can be split

        an element is dominant if count[el] > len(nums)//2
        we split at index k to get nums[:k+1], nums[k+1:], then use the prefix array to check if x is still dominant
        """
        dom, highest = -1, -1
        count = defaultdict(int)
        for i, n in enumerate(nums):
            count[n] += 1
            if count[n] > highest:
                dom, highest = n, count[n]

        N = len(nums)
        prefix = [0] * N
        for i in range(N):
            prefix[i] = (prefix[i-1] if i > 0 else 0) + int(nums[i] == dom)

        # k is the index where the left split array ends
        # since we are looking for the minimum index, return the first valid occurrence
        for k in range(0, N-1):
            leftDom = prefix[k] > (k+1)//2
            rightDom = prefix[-1] - prefix[k] > (N-(k+1))//2
            # print(nums[:k+1], nums[k+1:],  prefix[k], prefix[-1]-prefix[k])
            if leftDom and rightDom:
                return k

        return -1


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 2, 2],
        [2, 1, 3, 1, 1, 1, 7, 1, 2, 1],
        [3, 3, 3, 3, 7, 2, 2],
        [1],
        [1, 2, 1, 1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumIndex(*puzzle))
