# 1671. Minimum Number of Removals to Make Mountain Array

from utils import chunk
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        longestIncreasing = [0] * N
        # find the longest increasing subsequence by extending from a
        # number if increasing - check every element nums[j] before nums[i]
        for i in range(N):
            best = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(longestIncreasing[j], best)
            longestIncreasing[i] = best + 1

        longestDecreasing = [0] * N
        # opposite of above to find longest decreasing subsequence
        for i in reversed(range(N)):
            best = 0
            for j in range(i + 1, N):
                if nums[j] < nums[i]:
                    best = max(longestDecreasing[j], best)
            longestDecreasing[i] = best + 1

        # designate each element in nums as pivot, then use the
        # longest in/decreasing subsequence lengths to determine the minumum
        # we add 1 to the number of removals since the pivot is double counted
        # <longest increasing> | pivot | <longest decreasing>
        result = float('inf')
        for i in range(1, N - 1):
            left, right = longestIncreasing[i], longestDecreasing[i]
            if left > 1 and right > 1:  # only include valid pivots
                mountain = left + right - 1
                result = min(N - mountain, result)

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 3, 1],
        [2, 1, 1, 5, 6, 2, 3, 1],
        [8, 7, 6, 5, 4, 1, 2, 1],
        [3, 1, 3, 2]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumMountainRemovals(*puzzle))
