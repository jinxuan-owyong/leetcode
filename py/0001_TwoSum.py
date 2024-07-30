# 1. Two Sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))  # retain original indices
        nums.sort(key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i <= j:
            required = target - nums[i][1]
            if required == nums[j][1]:
                return [nums[i][0], nums[j][0]]
            if required < nums[j][1]:
                j -= 1
            else:
                i += 1


"""
Runtime
70
ms
Beats
42.51%
of users with Python3
Memory
17.95
MB
Beats
9.47%
of users with Python3
5
"""
