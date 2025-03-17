# 2206. Divide Array Into Equal Pairs

from utils import chunk
from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        return all(map(lambda x: count[x] % 2 == 0, count))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [3, 2, 3, 2, 2, 2],
        [1, 2, 3, 4]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().divideArray(*puzzle))
