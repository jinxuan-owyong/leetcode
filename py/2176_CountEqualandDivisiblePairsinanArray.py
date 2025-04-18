# 2176. Count Equal and Divisible Pairs in an Array

from utils import chunk
from typing import List
from collections import defaultdict


class Solution:
    # group equal elements together
    def countPairs(self, nums: List[int], k: int) -> int:
        equal = defaultdict(list)
        for i, n in enumerate(nums):
            equal[n].append(i)

        result = 0
        for n, indices in equal.items():
            for i in range(len(indices)-1):
                for j in range(i+1, len(indices)):
                    if (indices[i]*indices[j]) % k == 0:
                        result += 1
        return result

    # brute force
    # def countPairs(self, nums: List[int], k: int) -> int:
    #     result = 0
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if (i*j) % k == 0 and nums[i] == nums[j]:
    #                 result += 1
    #     return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [3, 1, 2, 2, 2, 1, 3],
        2,
        [1, 2, 3, 4],
        1,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().countPairs(*puzzle))
