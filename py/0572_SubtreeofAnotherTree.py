# 572. Subtree of Another Tree

from utils import chunk, toTree, printTree
from typing import Optional
from classes import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return root and self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [3, 4, 5, 1, 2],
        [4, 1, 2],
        [3, 4, 5, 1, 2, None, None, None, None, 0],
        [4, 1, 2],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().isSubtree(*map(toTree, puzzle)))
