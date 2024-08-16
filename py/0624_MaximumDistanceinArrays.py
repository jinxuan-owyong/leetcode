# 624. Maximum Distance in Arrays

from typing import List
import heapq


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # find first 2 smallest/largest elements
        minEl, maxEl = [], []
        for i, array in enumerate(arrays):
            heapq.heappush(minEl, [-array[0], i])  # keep smaller
            heapq.heappush(maxEl, [array[-1], i])  # keep larger
            if i > 1:
                heapq.heappop(minEl)
                heapq.heappop(maxEl)

        minEl[0][0] *= -1
        minEl[1][0] *= -1
        minEl.sort()
        maxEl.sort(reverse=True)

        # from the same array
        if maxEl[0][1] == minEl[0][1]:
            first = maxEl[0][0] - minEl[1][0]
            second = maxEl[1][0] - minEl[0][0]
            return max(first, second)

        return maxEl[0][0] - minEl[0][0]


if __name__ == "__main__":
    puzzles = [
        [[1, 2, 3], [4, 5], [1, 2, 3]],
        [[1], [1]],
        [[3], [9]],
        [[1, 4], [0, 5]]
    ]
    for puzzle in puzzles:
        print(Solution().maxDistance(puzzle))
