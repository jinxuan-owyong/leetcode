# 689. Maximum Sum of 3 Non-Overlapping Subarrays

from utils import chunk
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        pre-calculate the sum of the overlapping subarrays -> sub[i] = sum(nums[i:i+k]) 
        in the first example, sub = [3, 3, 3, 8, 13, 12, 6]
        then find the prefix maximum from left and right
        the last pass involves using the iterator as the middle subarray, and determining
        the maximum using left[i-1] and right[i+1]
        """
        if len(nums) < 3*k:
            return []

        curr = sum(nums[:k])
        sub = [curr]

        # calculate subarray sums using sliding window
        for i in range(len(nums)-k):
            curr += nums[i+k] - nums[i]
            sub.append(curr)

        left = [0] * len(sub)
        right = [len(sub) - 1] * len(sub)

        # determine prefix max (stores index)
        # note: since we want lexicographically smallest result, left uses > while right uses >=
        for i in range(1, len(sub)):
            left[i] = i if sub[i] > sub[left[i-1]] else left[i-1]
        for i in reversed(range(0, len(sub) - 1)):
            right[i] = i if sub[i] >= sub[right[i+1]] else right[i+1]

        result, total = [], 0
        for i in range(k, len(sub) - k):
            if (temp := sub[left[i-k]] + sub[i] + sub[right[i+k]]) > total:
                result = [left[i-k], i, right[i+k]]
                total = temp

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 1, 2, 6, 7, 5, 1],
        2,
        [1, 2, 1, 2, 1, 2, 1, 2, 1],
        2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxSumOfThreeSubarrays(*puzzle))
