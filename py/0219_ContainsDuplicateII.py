# 219. Contains Duplicate II

from utils import chunk
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        abs(i-j) <= k just means that it is a window size of at most k
        then we can use a fixed size sliding window to check there are any
        elements that are equal
        """
        window = set()
        i = 0
        for j in range(len(nums)):
            while j-i > k:
                window.remove(nums[i])
                i += 1
            if nums[j] in window:
                return True
            window.add(nums[j])
        return False


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3, 1],
        3,
        [1, 0, 1, 1],
        1,
        [1, 2, 3, 1, 2, 3],
        2,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().containsNearbyDuplicate(*puzzle))
