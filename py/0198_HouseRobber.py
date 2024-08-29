# 198. House Robber

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def visit(i: int, total: int):
            if i >= len(nums):
                return total
            if (i, total) in cache:
                return cache[(i, total)]

            steal = visit(i + 2, total + nums[i])
            skip = visit(i + 1, total)

            cache[(i, total)] = max(steal, skip)
            return cache[(i, total)]

        return visit(0, 0)


if __name__ == "__main__":
    puzzles = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [4, 1, 1, 8]
    ]
    for puzzle in puzzles:
        print(Solution().rob(puzzle))
