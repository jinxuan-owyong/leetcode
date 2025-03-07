# 2523. Closest Prime Numbers in Range

from utils import chunk
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        N = 1_000_000
        isPrime = [True] * (N+1)

        # sieve of eratosthenes
        p = 2
        while (p * p <= N):
            if isPrime[p]:
                # Update all multiples of p
                for i in range(p * p, N+1, p):
                    isPrime[i] = False
            p += 1

        # only consider adjacent pairs since any other pairs will have a further distance
        distance = float('inf')
        pair = [-1, -1]

        # find the first valid prime
        i, j = -1, max(2, left)
        while i == -1 and j < len(isPrime):
            i = j if isPrime[j] else -1
            j += 1

        for j in range(i+1, min(N+1, right+1)):
            if isPrime[j]:
                if j - i < distance:
                    pair = [i, j]
                    distance = j - i
                i = j

        return pair if pair[0] >= 0 and pair[1] >= 0 else [-1, -1]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        10, 19,
        4, 6,
        999998,
        1000000
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().closestPrimes(*puzzle))
