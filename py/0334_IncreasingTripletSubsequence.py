# 334. Increasing Triplet Subsequence

from utils import chunk
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        keep track of smallest and second smallest with 2 values
        in each iteration, only either of first or second will be updated
        if we have a decreasing sequence, then only first is updated
        if there are only increasing sequences, then at most the second case will be evaluated
        to reach the third case, we need first < second < nums[i] to be true, so return immediately if we ever reach the else case

        however, we cannot only use <, since it would result in [1,1,1] becoming
        true, same for [1,2,2]. hence <= is used in the checks
        """
        first, second = float('inf'), float('inf')
        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 1, 5, 0, 4, 6],
        [1, 2, 1, 3],
        [1, 2, -10, -8, -7],
        [1, 1, 1],
        [1, 2, 2]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().increasingTriplet(*puzzle))
