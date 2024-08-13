# 39. Combination Sum

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(i: int, total: int):
            if total == target:
                result.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i, total + candidates[i])
            curr.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    puzzles = [
        ([2, 3, 6, 7], 9),
        ([2, 3, 5], 8),
        ([2], 1)
    ]
    for puzzle in puzzles:
        print(Solution().combinationSum(*puzzle))
