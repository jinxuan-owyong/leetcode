# 2873. Maximum Value of an Ordered Triplet I

from utils import chunk
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # brute force
        N = len(nums)
        result = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    result = max(
                        (nums[i] - nums[j]) * nums[k],
                        result
                    )
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [12, 6, 1, 2, 7],
        [1, 10, 3, 4, 19],
        [1, 2, 3],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maximumTripletValue(*puzzle))
