# 983. Minimum Cost For Tickets

from utils import chunk
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def travel(i: int) -> int:
            if i in cache:
                return cache[i]
            if i == len(days):
                return 0

            d1, d7, d30 = i+1, i+1, i+1
            # find the next index d1/d7/d30 that gives us the next date we have to purchase
            # tickets for if we choose to buy an x-day ticket
            while d7 < len(days) and days[i] + 7 > days[d7]:
                d7 += 1
            while d30 < len(days) and days[i] + 30 > days[d30]:
                d30 += 1

            curr = [
                travel(d1) + costs[0],
                travel(d7) + costs[1],
                travel(d30) + costs[2],
            ]

            cache[i] = min(curr)
            return cache[i]
        return travel(0)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 4, 6, 7, 8, 20],
        [2, 7, 15],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
        [2, 7, 15],
        list(range(1, 366)),
        [2, 6, 28]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().mincostTickets(*puzzle))
