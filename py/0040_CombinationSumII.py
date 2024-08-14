# 40. Combination Sum II

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        curr = []

        def backtrack(i: int, total: int):
            if total == target:
                result.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            curr.pop()

            # prevent multiple of the same candidates from being chosen
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[j - 1]:
                j += 1
            backtrack(j, total)

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    puzzles = [
        ([10, 1, 2, 7, 6, 1, 5], 8),
        ([2, 5, 2, 1, 2], 5),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27)
    ]
    for puzzle in puzzles:
        print(Solution().combinationSum2(*puzzle))
