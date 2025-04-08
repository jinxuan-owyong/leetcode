# 3396. Minimum Number of Operations to Make Elements in Array Distinct

from utils import chunk
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visited = [False] * 101
        for i in reversed(range(len(nums))):
            if visited[nums[i]]:
                # count number of 3-removals required to reach here, including the current cell
                return (i+3)//3
            visited[nums[i]] = True

        # all values are unique
        return 0

# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         count = [0] * 101
#         duplicate = 0
#         for n in nums:
#             count[n] += 1
#             if count[n] > 1:
#                 duplicate += 1

#         i = 0
#         operations = 0
#         while duplicate:
#             operations += 1

#             if len(nums)-i < 3:
#                 i = len(nums)-1
#                 break

#             for j in range(i, i+3):
#                 if count[nums[j]] > 1:
#                     duplicate -= 1
#                 count[nums[j]] -= 1
#                 i += 1

#         return operations


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, 4, 2, 3, 3, 5, 7],
        [4, 5, 6, 4, 4],
        [6, 7, 8, 9],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumOperations(*puzzle))
