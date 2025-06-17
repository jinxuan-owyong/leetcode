# 46. Permutations

from utils import chunk
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        added = set()

        def backtrack():
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            for n in nums:
                if n not in added:
                    added.add(n)
                    curr.append(n)
                    backtrack()
                    curr.pop()
                    added.remove(n)
        backtrack()
        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().permute(*puzzle))
