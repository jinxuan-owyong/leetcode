# 1014. Best Sightseeing Pair

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # since i < j, then we iterate indices 1..n - 1
        # we keep track of maxAddIndexSoFar since any smaller value does not improve the score
        result = 0
        maxAddIndexSoFar = values[0]

        for i in range(1, len(values)):
            addIndex = values[i] + i
            subtractIndex = values[i] - i

            result = max(result, maxAddIndexSoFar + subtractIndex)
            maxAddIndexSoFar = max(maxAddIndexSoFar, addIndex)

        return result


if __name__ == "__main__":
    puzzles = [
        [8, 1, 5, 2, 6],
        [1, 2]
    ]
    for puzzle in puzzles:
        print(Solution().maxScoreSightseeingPair(puzzle))
