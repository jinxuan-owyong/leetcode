# 199. Binary Tree Right Side View

from typing import Optional, List
from classes import TreeNode
from utils import toTree
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal to get the right most element, can be in left subtree
        result = []
        q = deque([root])
        while q:
            right = None
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr:
                    continue
                right = curr.val
                q.extend([curr.left, curr.right])
            if right != None:
                result.append(right)
        return result


if __name__ == "__main__":
    puzzles = [
        [1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2],
        [0, 1, 2, None, 3, 4, None, None, 5, 9, None, None, 6, 10, None]
    ]
    for puzzle in puzzles:
        print(Solution().rightSideView(toTree(puzzle)))
