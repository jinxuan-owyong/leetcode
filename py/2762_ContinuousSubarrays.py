# 2762. Continuous Subarrays

from utils import chunk
from typing import List
import heapq


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total = 0
        lo, hi = [], []
        i = 0

        for j in range(len(nums)):
            # use a min/max heap to quickly access the range of a window
            heapq.heappush(lo, (nums[j], j))
            heapq.heappush(hi, (-nums[j], j))

            # shrink window until constraints are met
            while hi and lo and -hi[0][0] - lo[0][0] > 2:
                # remove indices that no longer belong to the window
                i += 1
                while hi and hi[0][1] < i:
                    heapq.heappop(hi)
                while lo and lo[0][1] < i:
                    heapq.heappop(lo)

            total += j - i + 1

        return total


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [5, 4, 2, 4],
        [1, 2, 3]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().continuousSubarrays(*puzzle))
