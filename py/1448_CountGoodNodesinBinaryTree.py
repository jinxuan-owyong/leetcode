# 1448. Count Good Nodes in Binary Tree

from utils import chunk
from utils import chunk, toTree
from classes import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, highest: int) -> int:
            if not node:
                return 0
            # pre-order traversal, node is counted if it is the highest so far
            count = 1 if node.val >= highest else 0
            # keep the largest value so far
            count += dfs(node.left, max(node.val, highest))
            count += dfs(node.right, max(node.val, highest))
            return count
        return dfs(root, -float('inf'))


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [3, 1, 4, 3, None, 1, 5],
        [3, 3, None, 4, 2],
        [1],
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().goodNodes(toTree(puzzle[0])))
