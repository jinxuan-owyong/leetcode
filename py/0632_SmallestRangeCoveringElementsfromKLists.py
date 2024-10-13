# 632. Smallest Range Covering Elements from K Lists

from utils import chunk
from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        First understand how we can find the smallest range in 2 lists
        [0, 9, 12, 20]
        [5, 18, 22, 30]
        Using 2 pointers, we start at 0 and 5 in each of list
        We keep track of the range between the two pointers at a given time
        In order to shrink the range, the only logical move is to increment
        the pointer to the smaller value
        We increment the pointers until we cannot increment further
        Then we have (0, 5) > (5, 9) > (9, 18) > (12, 18) > (18, 20) > (20, 22)

        Using this idea, we apply it to K lists
        To determine the smallest value of our pointer, we use a min heap 
        consisting (val, numIdx, arrIdx) to sort the pointers by value
        """

        pointers = [(arr[0], 0, i) for i, arr in enumerate(nums)]
        heapq.heapify(pointers)

        currRange = [pointers[0][0], max(pointers)[0]]
        smallest = currRange.copy()

        # we cannot increment further if the min pointer is at the end of its array
        while True:
            minVal, minNumIdx, minArrIdx = heapq.heappop(pointers)
            if minNumIdx == len(nums[minArrIdx]) - 1:
                break

            minNumIdx += 1
            minVal = nums[minArrIdx][minNumIdx]

            # consider whether incrementing the min pointer results in
            # itself becoming the new min range
            # the second pointer becoming the min range
            # itself becoming the new max range
            currRange = [min(minVal, pointers[0][0]),
                         max(minVal, currRange[1])]

            # store new range if smaller
            s1, e1 = currRange
            s2, e2 = smallest
            if e1 - s1 < e2 - s2:
                smallest = currRange.copy()

            heapq.heappush(pointers, (minVal, minNumIdx, minArrIdx))

        return smallest


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],
        [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
        [[1], [2], [5], [4], [9]],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().smallestRange(*puzzle))
