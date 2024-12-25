# 515. Find Largest Value in Each Tree Row

from utils import chunk, toTree
from typing import Optional, List
from classes import TreeNode
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            curr = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                curr = max(curr, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr)

        return result


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 3, 2, 5, 3, None, 9],
        [1, 2, 3],
        [],
        [1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().largestValues(toTree(puzzle[0])))
