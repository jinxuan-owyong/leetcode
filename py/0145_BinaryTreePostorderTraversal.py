# 145. Binary Tree Postorder Traversal

from typing import Optional, List
from classes import TreeNode
from utils import toTree


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

        traverse(root)
        return result


if __name__ == "__main__":
    puzzles = [
        [1, None, 2, 3],
        [],
        [1],
    ]
    for puzzle in puzzles:
        print(Solution().postorderTraversal(toTree(puzzle)))
