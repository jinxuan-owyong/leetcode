# 2461. Maximum Sum of Distinct Subarrays With Length K

from utils import chunk
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}  # hash map to keep track of whether element has duplicate
        total = 0

        def incrementNum(n: int):
            nonlocal total
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
            total += n

        for j in range(k):
            incrementNum(nums[j])

        # first case has the maximum
        result = total if len(freq) == k else 0

        for i in range(len(nums) - k):
            j = i + k
            removeNum, addNum = nums[i], nums[i + k]
            incrementNum(addNum)

            freq[removeNum] -= 1
            total -= removeNum
            if freq[removeNum] == 0:
                del freq[removeNum]

            if len(freq) == k:  # elements in window are distinct
                result = max(total, result)

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 5, 4, 2, 9, 9, 9], 3,
        [4, 4, 4], 3,
        [1, 5, 4, 2, 9], 3,
        [9, 2, 4, 5, 1], 3,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maximumSubarraySum(*puzzle))
