# 300. Longest Increasing Subsequence

from utils import chunk
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        brute force: determine the LIS for nums[i:]
        at each element, we make a decision on whether to include or ignore 
        the element, depending if it is larger than the previous value
        at the worst case we can have 2 branches at every element, giving us 
        an O(2^N) time complexity


        we can eliminate some repetition of work, since only 
        value < nums[i] is accepted for increasing subsequences for nums[i:]

        [9 1 4 2 3 3 7]
        from position 0, the LIS is [9]
        from position 1, the LIS is [1,2,3,7]
        from position 3, the LIS is [2,3,7]
        we can eliminate the repeated work to obtain [2,3,7] since we would have
        encountered this case when checking for subsequences after element 1

        extend the idea to starting from position 6, then we get [7]
        we know that there are no elements larger than 7, so LIS = 1
        from position 5, we can check nums[5+1:] for LIS
        if nums[5] < nums[i], then we have LIS nums[5] + LIS[i]
        otherwise nums[5] is its own LIS
        this yields a O(N^2) dp approach, where we recursively build upon
        the previous LIS to get a longer one

        dp[i] is the length of the LIS starting from i
        since LIS may not start from the first element, return max of dp
        """
        # bottom-up
        dp = [1] * len(nums)
        for i in reversed(range(len(nums)-1)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(
                        dp[i],
                        1 + dp[j]
                    )
        return max(dp)

        # # top-down
        # cache = {}
        # def dfs(i):
        #     if i in cache:
        #         return cache[i]
        #     if i == len(nums):
        #         return 0

        #     result = 1 # nums[i] itself
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             result = max(result, 1 + dfs(j))

        #     cache[i] = result
        #     return result

        # longest = 0
        # for i in range(len(nums)):
        #     longest = max(longest, dfs(i))
        # return longest


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().lengthOfLIS(*puzzle))
