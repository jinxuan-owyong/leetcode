# 112. Path Sum

from classes import TreeNode
from utils import toTree
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def findPath(root: Optional[TreeNode], sum: int):
            if not root:
                return sum == targetSum

            left = findPath(root.left, sum + root.val)
            right = findPath(root.right, sum + root.val)

            # note: not having a left/right subtree is not
            # enough to determine whether a node is a leaf
            if root.left and not root.right:
                return left
            if root.right and not root.left:
                return right

            return left or right

        return findPath(root, 0)


if __name__ == "__main__":
    puzzles = [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22),
        ([1, 2, 3], 5),
        ([], 0),
        ([1, 2], 1),
        ([1, 2, 3], 3),
    ]
    for root, targetSum in puzzles:
        print(Solution().hasPathSum(toTree(root), targetSum))

"""
Runtime
41
ms
Beats
55.98%
of users with Python3
Memory
17.43
MB
Beats
39.74%
of users with Python3
6
"""
