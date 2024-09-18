# 179. Largest Number

from utils import chunk
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def score(n1: int, n2: int) -> int:
            s1, s2 = str(n1), str(n2)
            if s1 == s2:
                return 0
            # joining s1 with s2 results in a larger integer
            # 12 vs 112 -> "12 > 112" since 12112 > 11212
            elif s1 + s2 > s2 + s1:
                return 1
            else:
                return -1

        # we want to penalise small numbers
        # the penalty is heavier if the digit in front
        nums.sort(key=cmp_to_key(score), reverse=True)

        # the largest number is 0, ignore repeated 0s
        if nums[0] == 0:
            return "0"
        
        return ''.join(map(str, nums))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [10, 2],
        [3, 30, 34, 5, 9],
        [909, 1, 9, 92],
        [100, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [12, 9, 92, 1]  # 992121 > 992112
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().largestNumber(*puzzle))
