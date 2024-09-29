# 1046. Last Stone Weight

from utils import chunk
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            result = abs(first - second)
            if result:
                heapq.heappush(stones, -result)

        return -stones[0] if len(stones) else 0


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 7, 4, 1, 8, 1],
        [1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().lastStoneWeight(*puzzle))
