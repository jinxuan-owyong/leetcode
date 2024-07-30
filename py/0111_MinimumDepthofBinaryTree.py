# 111. Minimum Depth of Binary Tree

from classes import TreeNode
from utils import toTree
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right + 1
        if right == 0:
            return left + 1
        return min(left, right) + 1


if __name__ == "__main__":
    puzzles = [
        [3, 9, 20, None, None, 15, 7],
        [2, None, 3, None, 4, None, 5, None, 6]
    ]
    for puzzle in puzzles:
        print(Solution().minDepth(toTree(puzzle)))

"""
Runtime
261
ms
Beats
46.32%
of users with Python3
Memory
43.61
MB
Beats
14.17%
of users with Python3
11
"""
