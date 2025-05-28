# 55. Jump Game

from utils import chunk
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        from each nums[i], we want to jump to the furthest position from current position
        either greedy or dfs or dynamic programming
        [1,2,0,1,0]
         ^ ^   ^   <-- take these since they are non-zero
        [1,2,1,0,1]
         ^ ^   ^   <-- we end up here regardless of the path we take
        if we iterate front to back, then we have to consider the different possible path branches

        alternatively, if start from the back,
        if we can reach index N-1 from N-2, then we just need to check if we can reach N-2
        otherwise we check if we can reach N-1 from N-3 and repeat this process until we reach 0
        we can reach a goal from index i if nums[i]+i, which is the furthest index from current step
        allows us to at least reach goal >= goal. if so, update goal to i
        """

        goal = len(nums)-1

        for i in reversed(range(len(nums)-1)):
            if nums[i]+i >= goal:
                goal = i

        return goal == 0

        # # top-down, TLE on leetcode
        # cache = {}
        # def dfs(i: int) -> bool:
        #     if i in cache:
        #         return cache[i]
        #     if i == len(nums)-1:
        #         return True
        #     steps = nums[i]
        #     for j in range(1, steps+1):
        #         cache[i+j] = dfs(i+j)
        #         if cache[i+j]:
        #             return True
        #     cache[i] = False
        #     return False

        # return dfs(0)


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().canJump(*puzzle))
