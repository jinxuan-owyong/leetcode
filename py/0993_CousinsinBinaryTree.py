# 993. Cousins in Binary Tree

from utils import chunk, toTree
from typing import Optional
from classes import TreeNode
from collections import deque


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, None)])

        while queue:
            childToParent = {}

            for _ in range(len(queue)):
                curr, parent = queue.popleft()
                childToParent[curr.val] = parent
                if curr.left:
                    queue.append((curr.left, curr))
                if curr.right:
                    queue.append((curr.right, curr))

            if x in childToParent and y in childToParent and childToParent[x] != childToParent[y]:
                return True

        return False


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        [1, 2, 3, 4], 4, 3,
        [1, 2, 3, None, 4, None, 5], 5, 4,
        [1, 2, 3, None, 4], 2, 3
    ]
    for puzzle in chunk(puzzles, testSize):
        root, x, y = puzzle
        print(Solution().isCousins(toTree(root), x, y))
