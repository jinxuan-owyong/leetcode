# 128. Longest Consecutive Sequence

from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = {i: 1 for i in range(n)}

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        # path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        # join the shorter tree to the taller tree
        if self.size[x] > self.size[y]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.size[rootY] = 0
        else:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            self.size[rootX] = 0


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uf = UnionFind(len(nums))
        numsIdx = {}

        for i in range(len(nums)):
            if nums[i] in numsIdx:
                continue
            if nums[i] - 1 in numsIdx:
                uf.union(i, numsIdx[nums[i] - 1])
            if nums[i] + 1 in numsIdx:
                uf.union(i, numsIdx[nums[i] + 1])
            numsIdx[nums[i]] = i

        return max(uf.size.values())


if __name__ == "__main__":
    puzzles = [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        [],
        [0, - 1]
    ]
    for puzzle in puzzles:
        print(Solution().longestConsecutive(puzzle))

"""
Runtime
526
ms
Beats
39.20%
of users with Python3
Memory
45.74
MB
Beats
5.01%
of users with Python3
40*
"""
