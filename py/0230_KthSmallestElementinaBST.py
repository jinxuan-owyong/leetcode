# 230. Kth Smallest Element in a BST

from utils import chunk, toTree
from typing import Optional
from classes import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        In a BST, root.left.val < root.val < root.right.val
        If we perform inorder traversal, we can easily find the kth smallest
        """
        result = -1
        i = 0
        stack = [root]

        def dfs(node):
            nonlocal i, result
            if not node or result != -1:
                return
            dfs(node.left)
            i += 1
            if i == k:
                result = node.val
                return
            dfs(node.right)

        dfs(root)
        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [3, 1, 4, None, 2], 1,
        [5, 3, 6, 2, 4, None, None, 1], 3,
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().kthSmallest(toTree(puzzle[0]), puzzle[1]))
