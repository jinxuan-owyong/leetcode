# 1497. Check If Array Pairs Are Divisible by k

from utils import chunk
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # if sum of each pair is divisible,
        # the sum of all pairs should be as well
        if sum(arr) % k > 0:
            return False

        count = {i: list() for i in range(k)}
        for num in arr:
            count[num % k].append(num)

        for n1 in count:
            # n1 requires n2 = (k - n1) % k as its key
            n2 = (k - n1) % k
            # count should match for all pairs to sum to k
            if len(count[n1]) != len(count[n2]):
                return False

        return True


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3, 4, 5, 10, 6, 7, 8, 9],
        5,
        [1, 2, 3, 4, 5, 6],
        7,
        [1, 2, 3, 4, 5, 6],
        10
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canArrange(*puzzle))
