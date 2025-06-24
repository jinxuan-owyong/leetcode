# 239. Sliding Window Maximum

from utils import chunk
from typing import List
import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque
        # hold valid indices for the window
        window = deque()
        result = []

        for i in range(len(nums)):
            # at any time, the right of the deque holds the largest value in the window
            # pop from the right of the deque until the incoming value becomes the largest
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)
            # remove indices once the window is past them
            while window[0] <= i-k:
                window.popleft()

            # start appending when we have at least k elements in the window
            if i >= k-1:
                result.append(nums[window[0]])

        return result

        # # heap
        # window = []
        # result = []

        # for i, n in enumerate(nums):
        #     # store values in a max heap
        #     heapq.heappush(window, (-n, i))

        #     # we are only concerned with the k-recent values
        #     # it is fine to have more than k values in the heap, as long as
        #     # the maximum is from within k elements
        #     while len(window) > k and window[0][1] <= i-k:
        #         heapq.heappop(window)

        #     if i >= k-1:
        #         result.append(-window[0][0])

        # return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 3, -1, -3, 5, 3, 6, 7],
        3,
        [1],
        1,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxSlidingWindow(*puzzle))
