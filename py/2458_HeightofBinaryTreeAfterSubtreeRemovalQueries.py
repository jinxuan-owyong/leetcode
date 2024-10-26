# 2458. Height of Binary Tree After Subtree Removal Queries

from utils import chunk, toTree
from typing import Optional, List
from classes import TreeNode


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heightAfterRemove = [0] * 100001  # maximum node value is 100000
        maxHeight = 0

        def traverseLR(curr: Optional[TreeNode], depth: int):
            nonlocal maxHeight
            if not curr:
                return
            # retain previous maxHeight, since that would be the
            # new maximum after removal of a node
            heightAfterRemove[curr.val] = maxHeight
            maxHeight = max(depth, heightAfterRemove[curr.val])
            traverseLR(curr.left, depth + 1)
            traverseLR(curr.right, depth + 1)

        def traverseRL(curr: Optional[TreeNode], depth: int):
            nonlocal maxHeight
            if not curr:
                return
            heightAfterRemove[curr.val] = max(
                maxHeight,
                heightAfterRemove[curr.val]
            )
            maxHeight = max(depth, maxHeight)
            traverseRL(curr.right, depth + 1)
            traverseRL(curr.left, depth + 1)

        # perform traversal in both root, left, right and root, right, left
        traverseLR(root, 0)
        maxHeight = 0
        traverseRL(root, 0)
        return [heightAfterRemove[q] for q in queries]


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7],
        [4],
        [5, 8, 9, 2, 1, 3, 7, 4, 6],
        [3, 2, 4, 8],
    ]
    for puzzle in chunk(puzzles, testSize):
        root, queries = puzzle
        print(Solution().treeQueries(toTree(root), queries))
