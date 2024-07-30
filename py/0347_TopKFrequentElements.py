# 347. Top K Frequent Elements

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [k for k, _ in count.most_common(k)]

        # heap = [(-v, k) for k, v in count.items()]
        # heapify(heap)
        # return [heappop(heap)[1] for _ in range(k)


if __name__ == "__main__":
    puzzles = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1)
    ]
    for puzzle in puzzles:
        print(Solution().topKFrequent(*puzzle))

"""
Runtime
87
ms
Beats
69.27%
of users with Python3
Memory
20.98
MB
Beats
83.48%
of users with Python3
3
"""
