# 862. Shortest Subarray with Sum at Least K

from utils import chunk
from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = float('inf')
        total = 0
        queue = deque()  # monotically increasing
        for i, n in enumerate(nums):
            total += n
            if total >= k:
                result = min(result, i + 1)

            # shrink window while it is greater than k, nums[i] can be negative,
            # which will cause the sum to increase rather than decrease
            while queue and total - queue[0][0] >= k:
                prefix, endIdx = queue.popleft()
                result = min(result, i - endIdx)

            # check end of queue to maintain monotonic increasing property
            while queue and queue[-1][0] >= total:
                queue.pop()

            queue.append((total, i))

        return -1 if result == float('inf') else result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1], 1,
        [1, 2], 4,
        [2, -1, 2], 3
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().shortestSubarray(*puzzle))
