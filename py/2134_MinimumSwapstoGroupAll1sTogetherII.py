# 2134. Minimum Swaps to Group All 1's Together II


from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = sum(nums)
        currOnes = sum(nums[:totalOnes])  # "1"s in the window
        swaps = 1E10

        i, j = 0, totalOnes - 1  # window size is the end result
        while i < len(nums):
            j = (i + totalOnes - 1) % len(nums)
            swaps = min(totalOnes - currOnes, swaps)
            currOnes += nums[(j + 1) % len(nums)] - nums[i]
            i += 1

        return swaps


if __name__ == "__main__":
    puzzles = [
        [0, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [1],
        [0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    ]
    for puzzle in puzzles:
        print(Solution().minSwaps(puzzle))

"""
Runtime
756
ms
Beats
33.56%
Memory
20.72
MB
Beats
29.05%
"""
