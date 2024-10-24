# 951. Flip Equivalent Binary Trees

from utils import chunk, toTree
from typing import Optional
from classes import TreeNode


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        # impossible to be flip equivalent if the roots or children do not match
        if not root1 or not root2 or root1.val != root2.val:
            return False

        # at each subroot, we attempt to "flip" the children to find flip equivalence
        dontFlip = self.flipEquiv(root1.left, root2.left) and \
            self.flipEquiv(root1.right, root2.right)
        flip = self.flipEquiv(root1.left, root2.right) and \
            self.flipEquiv(root1.right, root2.left)

        return dontFlip or flip


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3, 4, 5, 6, None, None, None, 7, 8],
        [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7],
        [],
        [],
        [],
        [1]
    ]
    for puzzle in chunk(puzzles, testSize):
        root1, root2 = puzzle
        print(Solution().flipEquiv(toTree(root1), toTree(root2)))
