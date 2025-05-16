# 416. Partition Equal Subset Sum

from utils import chunk
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        we cannot have any remainder if we want to split into 2 equal partitions, hence odd total is out
        if we backtrack to find the partition, MLE
        use a bool list to keep track of numbers that can be partitioned up to total/2
        alternatively use a hashset to find values of dp[j] which are true
        """
        total = sum(nums)
        if total % 2:
            return False

        # we can form a new partition with nums[i] if dp[j] is true, dp[j+nums[i]] is also true
        dp = [False] * ((total//2)+1)
        dp[0] = True
        for i in range(len(nums)):
            # edge case: if we use front to back, then if nums[i] = 1, whole dp array becomes True, case 3 will fail without this
            for j in reversed(range(len(dp))):
                if dp[j] and j+nums[i] < len(dp):
                    dp[j+nums[i]] = True
        return dp[-1]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 5, 11, 5],
        [1, 2, 3, 5],
        [1, 2, 5],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canPartition(*puzzle))
