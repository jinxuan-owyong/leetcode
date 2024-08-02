# 27. Remove Element

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return j + 1


if __name__ == "__main__":
    puzzles = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        ([], 1),
        ([0], 1),
        ([1], 1)
    ]
    for puzzle in puzzles:
        print(Solution().removeElement(*puzzle))
        print(puzzle)

"""
Runtime
35
ms
Beats
73.81%
Memory
16.63
MB
Beats
22.20%
"""
