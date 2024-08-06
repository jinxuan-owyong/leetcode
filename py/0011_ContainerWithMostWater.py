# 11. Container With Most Water


from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i, j = 0, len(heights) - 1
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            result = max(result, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return result


if __name__ == "__main__":
    puzzles = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1]
    ]
    for puzzle in puzzles:
        print(Solution().maxArea(puzzle))
