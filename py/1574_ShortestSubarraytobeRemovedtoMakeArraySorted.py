# 1574. Shortest Subarray to be Removed to Make Array Sorted

from utils import chunk
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        first search from the front and back to find the longest non-decreasing subarray
        [1, 2, 3, 10, 4, 2, 3, 5]
        [    L     ]  M  [  R   ]
        we get 2 arrays left = arr[0:4] and right = arr[5:]
        to find the best shortest subarray to remove, we use a sliding window based on the values from above
        if the resulting array is non-decreasing: arr[i] <= arr[j], we take note of the middle subarray removed
        and shrink the window. otherwise we expand the window
        [1, 2, 3, 10, 4, 2, 3, 5]
         0  [    4    ]  5
            1  [   3  ]  5
               2         5
               2  [  3   ]  6
                  3         6
                  3            7
        """
        N = len(arr)
        left, right = 0, N - 1
        while left < N - 1:
            if arr[left] > arr[left + 1]:
                break
            left += 1

        while right > 0:
            if arr[right - 1] > arr[right]:
                break
            right -= 1

        if left == N - 1:  # already sorted
            return 0

        # determine the middle part to remove
        result = min(right, N - left - 1)
        i, j = 0, right
        while i <= left and j < N:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, 10, 4, 2, 3, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 3],
        [1, 2, 3, 8, 7, 1, 2, 3],
        [2, 2, 2, 1, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().findLengthOfShortestSubarray(*puzzle))
