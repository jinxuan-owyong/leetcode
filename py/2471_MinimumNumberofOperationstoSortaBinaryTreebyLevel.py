# 2471. Minimum Number of Operations to Sort a Binary Tree by Level

from utils import chunk, toTree
from typing import Optional
from classes import TreeNode
from collections import deque


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # tree has unique values
        level = deque([root])
        operations = 0

        while level:  # BFS
            pointer = {node.val: node for node in level}
            correct = sorted([(x.val, i) for i, x in enumerate(level)])

            for i in range(len(level)):
                curr = level.popleft()
                # if not in correct position, swap current value with node at its actual position
                if correct[i][0] != curr.val:
                    operations += 1
                    # locate where the correct value is and swap it with the incorrectly located node
                    a = pointer[curr.val]
                    b = pointer[correct[i][0]]
                    a.val, b.val = b.val, a.val
                    pointer[a.val] = a
                    pointer[b.val] = b

                if curr.left:
                    level.append(curr.left)
                if curr.right:
                    level.append(curr.right)

        return operations


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10],
        [1, 3, 2, 7, 6, 5, 4],
        [1, 2, 3, 4, 5, 6]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumOperations(toTree(puzzle[0])))
