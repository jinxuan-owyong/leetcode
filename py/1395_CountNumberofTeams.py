# 1395. Count Number of Teams

from typing import List


# https://www.youtube.com/watch?v=zONHzIqCr-o
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for j in range(1, len(rating) - 1):
            leftSmaller, leftLarger, rightSmaller, rightLarger = 0, 0, 0, 0

            for i in range(0, j):
                if rating[i] < rating[j]:
                    leftSmaller += 1
                elif rating[i] > rating[j]:
                    leftLarger += 1

            for k in range(j + 1, len(rating)):
                if rating[j] < rating[k]:
                    rightLarger += 1
                elif rating[j] > rating[k]:
                    rightSmaller += 1

            result += leftSmaller * rightLarger
            result += leftLarger * rightSmaller

        return result


if __name__ == "__main__":
    puzzles = [
        [2, 5, 3, 4, 1],
        [2, 1, 3],
        [1, 2, 3, 4]
    ]
    for puzzle in puzzles:
        print(Solution().numTeams(puzzle))

"""
Runtime
489
ms
Beats
57.12%
Memory
16.68
MB
Beats
66.67%
"""
