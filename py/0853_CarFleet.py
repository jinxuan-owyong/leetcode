# 853. Car Fleet

from utils import chunk
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first car (highest position) of the fleet affects speed of all cars behind
        # a car can catch up with one another if it has a faster speed and there is sufficient distance
        # at position[i], there is (target-position[i])/speed[i] time remaining for the fleet nearest to the target
        # based on time remaining, we group cars that will catch up to the current car
        cars = sorted([(p, i) for i, p in enumerate(position)], reverse=True)
        fleets = 0
        c = 0
        while c < len(cars):
            p1, i1 = cars[c]
            remainingTime = (target-p1)/speed[i1]
            c += 1
            # remove all the cars that can catch up with the car nearest to the target
            while c < len(cars):
                p2, i2 = cars[c]
                if (speed[i2]*remainingTime + p2) >= target:
                    c += 1
                else:
                    break
            fleets += 1
        return fleets


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        12,
        [10, 8, 0, 5, 3],
        [2, 4, 1, 1, 3],
        10,
        [3],
        [3],
        100,
        [0, 2, 4],
        [4, 2, 1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().carFleet(*puzzle))
