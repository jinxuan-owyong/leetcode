# 199. Binary Tree Right Side View

from typing import Optional, List
from classes import TreeNode
from utils import toTree
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([(root, 1)])  # node, level

        # level-order traversal
        while queue:
            node, level = queue.popleft()
            # last in queue or last in level
            if not queue or queue[0][1] == level + 1:
                result.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result


if __name__ == "__main__":
    puzzles = [
        [1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2]
    ]
    for puzzle in puzzles:
        print(Solution().rightSideView(toTree(puzzle)))
