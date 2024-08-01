# 15. 3Sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):  # O(N)
            target = -nums[i]
            j, k = i + 1, len(nums) - 1

            # prevent i duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            # 2Sum, multiple values - O(N)
            while j < k:
                total = nums[j] + nums[k]
                if total == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # prevent j duplicates
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
                elif total < target:
                    j += 1
                else:
                    k -= 1

        return result


if __name__ == "__main__":
    puzzles = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0, 0],
        [-2, -2, 0, 2, 2]
    ]
    for puzzle in puzzles:
        print(Solution().threeSum(puzzle))

"""
Runtime
607
ms
Beats
82.74%
Memory
20.67
MB
Beats
65.34%
"""
