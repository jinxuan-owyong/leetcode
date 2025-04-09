# 3375. Minimum Operations to Make Array Values Equal to K

from utils import chunk
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        An integer h is called valid if all values in the array that are strictly greater than h are identical.
        if a is the largest integer and b is the second largest, then a < h < b

        For each index i where nums[i] > h, set nums[i] to h.
        => since h is smaller than the largest element, we can convert the largest into the second largest element
        => repeat until all elements are <= k

        Count the number of unique elements that are larger than k
        not possible if k > smallest element
        """
        seen = [False] * 101
        operations = 0
        for n in nums:
            if not seen[n]:
                if n > k:
                    operations += 1
                seen[n] = True
        return operations if k <= min(nums) else -1


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [5, 2, 5, 4, 5],
        2,
        [2, 1, 2],
        2,
        [9, 7, 5, 3],
        1,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minOperations(*puzzle))
