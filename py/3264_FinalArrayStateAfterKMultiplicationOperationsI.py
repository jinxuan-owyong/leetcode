# 3264. Final Array State After K Multiplication Operations I

from typing import List
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [[x, i] for i, x in enumerate(nums)]
        heapq.heapify(pq)

        for _ in range(k):
            smallest = heapq.heappop(pq)
            smallest[0] *= multiplier
            nums[smallest[1]] = smallest[0]
            heapq.heappush(pq, smallest)

        return nums


if __name__ == "__main__":
    puzzles = [
        ([2, 1, 3, 5, 6], 5, 2),
        ([1, 2], 3, 4)
    ]
    for puzzle in puzzles:
        print(Solution().getFinalState(*puzzle))
