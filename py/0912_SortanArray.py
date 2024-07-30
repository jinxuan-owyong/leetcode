# 912. Sort an Array

from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def randomQuickSort(i: int, j: int) -> None:
            if i >= j:
                return

            pivot = random.randint(i, j)
            nums[i], nums[pivot] = nums[pivot], nums[i]  # swap

            # [pivot][low][high]...
            highStart = i + 1
            for k in range(i + 1, j + 1):
                # add randomness to distribute equal values
                if nums[k] == nums[i] and random.randint(0, 1) == 1:
                    continue
                # the "high" partition may contain the pivot
                elif nums[k] <= nums[i]:
                    nums[k], nums[highStart] = nums[highStart], nums[k]
                    highStart += 1

            nums[i], nums[highStart - 1] = nums[highStart - 1], nums[i]
            randomQuickSort(i, highStart - 1)
            randomQuickSort(highStart, j)

        randomQuickSort(0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    puzzles = [
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [1, 10, 9, 8, 7, 6, 5, 4, 3, 2],
        [1],
        [3, 2, 5, 1],
        # list(range(50000)),
        [2 for _ in range(10000)]
    ]
    for puzzle in puzzles:
        print(Solution().sortArray(puzzle))

"""
Runtime
1958
ms
Beats
5.02%
Memory
36.22
MB
Beats
9.01%
"""
