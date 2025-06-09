# 124. Binary Tree Maximum Path Sum

from utils import chunk, toTree, printTree
from typing import Optional
from classes import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        in a path, we can only have 1 "split", where one of the (sub)roots joins its children
        from each possible subroot, we can take the best path without splitting
        after evaluating each subroot, we keep 2 of the values
        - the maximum path sum so far, if we choose to include the current root
        - best path without splitting, including the current root, or 0 if negative to exclude all below
         """
        best = [root.val]

        def dfs(curr):  # returns best path without splitting, so that we can join further up the tree
            if not curr:
                return 0
            leftBranch = max(
                dfs(curr.left),
                0,  # prune branch since it's negative
            )
            rightBranch = max(
                dfs(curr.right),
                0,
            )
            best[0] = max(
                best[0],
                curr.val + leftBranch + rightBranch,
            )
            return curr.val + max(leftBranch, rightBranch)
        dfs(root)
        return best[0]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3],
        [-10, 9, 20, None, None, 15, 7],
        [-3],
        [1, -2, 3],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maxPathSum(toTree(puzzle[0])))
