# 2594. Minimum Time to Repair Cars

from utils import chunk
from typing import List
import math


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        binary search for the time taken to repair
        given the same amount of time for each mechanic, calculate how many cars they can repair
        n cars takes r * n^2 minutes => floor((time / r)^0.5) cars / time
        """
        i, j = 1, max(ranks)*cars*cars

        while i <= j:
            time = i + (j-i)//2
            carsFixed = sum(math.floor(math.sqrt(time / r)) for r in ranks) 
            if carsFixed >= cars:
                j = time-1 
            else:
                i = time+1

        return i



if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [4, 2, 3, 1],
        10,
        [5, 1, 8],
        6,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().repairCars(*puzzle))
