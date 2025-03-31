# 2551. Put Marbles in Bags

from utils import chunk
from typing import List
import heapq


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        bag[i, j] has cost weights[i] + weights[j] -> split into k subarrays
        score = (weights[0] + weights[i]) + (weights[i+1] + weights[j]) + (weights[j+1] + weights[k]) + ...
        result = max - min score 

        the first and last bag has one fixed cost (start/end of weights) -> these can be left out in the result since always unchanged
        for a split at weights[i:j+1], the variable cost is weights[j] + weights[j+1]
        consider the top k-1 split positions in the array, where each split is ranked by the variable cost
        """
        minHeap = []  # retains top k-1 max splits
        maxHeap = []  # retains bottom k-1 min splits
        for i in range(len(weights)-1):
            heapq.heappush(minHeap, (weights[i] + weights[i+1], i))
            heapq.heappush(maxHeap, (-weights[i] - weights[i+1], i))

            if len(minHeap) > k-1:
                heapq.heappop(minHeap)
                heapq.heappop(maxHeap)

        difference = 0
        for i in range(k-1):
            difference += minHeap[i][0]  # max split
            difference -= -maxHeap[i][0]  # min split

        return difference


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 3, 5, 1],
        2,
        [1, 3],
        2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().putMarbles(*puzzle))
