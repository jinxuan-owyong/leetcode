# 719. Find K-th Smallest Pair Distance

from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countNumPairsLessThanX(x: int) -> int:
            # nums is sorted
            count = 0

            # sliding window
            i = 0
            for j in range(len(nums)):
                while nums[j] - nums[i] > x:
                    i += 1
                count += (j - i)

            return count

        nums.sort()
        # search space ranges from 0 to max(nums)
        # since we find distance between pairs
        i, j = 0, max(nums)

        # in each iteraton, we count the number of pairs that are
        # less than or equal to mid using binary search
        while i < j:
            mid = (i + j) // 2
            count = countNumPairsLessThanX(mid)
            # it is not possible to find kth smallest pair if the number of pairs <= mid
            # is less than k, hence we do not need to search the remaining "left" portion
            if count < k:
                i = mid + 1
            # if we obtain a count > k, we do not know if  0...count-1 value
            # contains a smaller distance between the pairs
            else:
                j = mid

        return i


if __name__ == "__main__":
    puzzles = [
        ([1, 1, 3], 1),
        ([1, 1, 1], 2),
        ([1, 6, 1], 3),
        ([1, 2, 2, 4, 5, 6, 7], 7),
        ([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18)
    ]
    for puzzle in puzzles:
        print(Solution().smallestDistancePair(*puzzle))
