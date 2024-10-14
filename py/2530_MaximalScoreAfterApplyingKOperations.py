# 2530. Maximal Score After Applying K Operations

from utils import chunk
from typing import List
import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)

        # use max heap to keep track of next best move
        # k log(n)
        for _ in range(k):
            curr = -heapq.heappop(nums)
            score += curr
            heapq.heappush(nums, -math.ceil(curr / 3))

        return score

if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [10, 10, 10, 10, 10],
        5,
        [1, 10, 3, 3, 3],
        3,
        [1, 10, 3, 3, 3],
        100
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxKelements(*puzzle))
