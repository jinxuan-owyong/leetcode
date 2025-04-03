# 2874. Maximum Value of an Ordered Triplet II

from utils import chunk
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        since value = (nums[i] - nums[j]) * nums[k]
        we want to maximise nums[i] and nums[k], but minimise nums[j]
        pre-calculate the prefix and suffix max arrays
        use this value to calculate in a single pass afterwards since we know the  
        largest "nums[i]" and largest "nums[k]" to the left and right of nums[j] respectively
        """
        N = len(nums)
        prefixMax = [0] * N
        suffixMax = [0] * N

        for i in range(N):
            prefixMax[i] = max(
                prefixMax[i-1] if i else nums[0],
                nums[i]
            )

        for i in reversed(range(N)):
            suffixMax[i] = max(
                suffixMax[i+1] if i < N-1 else nums[-1],
                nums[i]
            )

        result = 0
        for i in range(1, N-1):
            result = max(
                (prefixMax[i-1] - nums[i]) * suffixMax[i+1],
                result
            )

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [12, 6, 1, 2, 7],
        [1, 10, 3, 4, 19],
        [1, 2, 3],
        [2, 3, 1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maximumTripletValue(*puzzle))
