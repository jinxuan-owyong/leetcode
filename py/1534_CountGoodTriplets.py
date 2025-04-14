# 1534. Count Good Triplets

from utils import chunk
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        return count


if __name__ == "__main__":
    testSize = 4
    puzzles = [
        [3, 0, 1, 1, 9, 7], 7, 2, 3,
        [1, 1, 2, 2, 3], 0, 0, 1
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countGoodTriplets(*puzzle))
