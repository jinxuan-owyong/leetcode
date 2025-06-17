# 973. K Closest Points to Origin

from utils import chunk
from typing import List
import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            dist = math.sqrt(x**2+y**2)
            # discard the n-k points furthest from the origin
            heapq.heappush(pq, (-dist, x, y))
            if len(pq) > k:
                heapq.heappop(pq)
        result = []
        for _, x, y in pq:
            result.append([x, y])
        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[1, 3], [-2, 2]],
        1,
        [[3, 3], [5, -1], [-2, 4]],
        2,]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().kClosest(*puzzle))
