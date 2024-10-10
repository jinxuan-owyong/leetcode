# 962. Maximum Width Ramp

from utils import chunk
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # monotonic decreasing stack to store the start of the ramp
        stack = []
        for i, n in enumerate(nums):
            if not stack or nums[stack[-1]] > n:
                stack.append(i)

        # from right to left, the first element in nums to be smaller than
        # the top of the stack forms the largest ramp for that start value
        largest = 0
        for right in reversed(range(len(nums))):
            if not stack:
                break
            while stack:
                left = stack[-1]
                if nums[left] <= nums[right]:
                    largest = max(right - left, largest)
                    stack.pop()
                else:
                    break

        return largest


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [6, 0, 8, 2, 1, 5],
        [9, 8, 1, 0, 1, 9, 4, 0, 4, 1],
        [1, 1],
        [1, 2],
        [2, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxWidthRamp(*puzzle))
