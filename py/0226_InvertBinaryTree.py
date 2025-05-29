# 226. Invert Binary Tree

from utils import chunk
from utils import chunk, toTree, printTree
from typing import Optional
from classes import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [4, 2, 7, 1, 3, 6, 9],
        [2, 1, 3],
        [],
    ]
    for puzzle in chunk(puzzles, testSize):
        printTree(Solution().invertTree(toTree(puzzle[0])))
        print()
