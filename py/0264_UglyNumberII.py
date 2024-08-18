# 264. Ugly Number II

import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set()
        heap = [1]
        i = 1

        while i < n:
            curr = heapq.heappop(heap)
            i += 1
            for factor in [2, 3, 5]:
                if curr * factor not in seen:
                    seen.add(curr * factor)
                    heapq.heappush(heap, curr * factor)

        return heap[0]


if __name__ == "__main__":
    puzzles = [
        *range(1, 11)
    ]
    for puzzle in puzzles:
        print(Solution().nthUglyNumber(puzzle))
