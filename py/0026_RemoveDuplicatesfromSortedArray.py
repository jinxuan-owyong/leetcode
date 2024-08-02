# 26. Remove Duplicates from Sorted Array


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[i - 1] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i  # length of array without duplicates


if __name__ == "__main__":
    puzzles = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]
    for puzzle in puzzles:
        print(Solution().removeDuplicates(puzzle))

"""
Runtime
78
ms
Beats
44.32%
Memory
17.84
MB
Beats
72.69%
"""
