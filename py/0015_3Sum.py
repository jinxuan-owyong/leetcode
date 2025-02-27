# 15. 3Sum

from utils import chunk
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            # prevent i duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # two sum
            target = -nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                curr = nums[j] + nums[k]
                # nums[i] + nums[j] + nums[k] = 0
                if curr == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # prevent j duplicates
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    # continue searching new pairs with same i
                elif curr < target:
                    j += 1
                else:
                    k -= 1

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [1, -1, -1, 0],
        [0, 0, 0],
        [0, 0, 0, 0],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().threeSum(*puzzle))
