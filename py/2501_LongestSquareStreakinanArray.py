# 2501. Longest Square Streak in an Array

from utils import chunk
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # given that upper bound of nums[i] is 10^5
        # the search space is restricted to up to streak length of 5
        # we just need to find a subsequence up to 10^5
        # 2, 4, 16, 256, 65536
        # 3, 9, 81, 6561
        # 4, 16, 256, 65536
        # 5, 25, 625
        # ...
        # 316, 99856

        validNums = set(nums)
        longestStreak = -1
        for start in nums:
            curr = start
            count = 1
            while curr < 100000 and curr ** 2 in validNums:
                count += 1
                curr **= 2
            if curr > start and count > longestStreak:
                longestStreak = count

        return longestStreak


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [4, 3, 6, 16, 8, 2],
        [2, 3, 5, 6, 7],
        [25, 4, 10, 2],
        [65536, 19, 8, 3, 4, 10, 2],
        [2, 256, 4, 16],
        [10, 6, 2, 256, 3, 65536, 50, 5, 4, 16],
        [i for i in range(2, 100000)]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestSquareStreak(*puzzle))
