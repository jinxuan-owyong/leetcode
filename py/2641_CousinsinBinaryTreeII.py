# 2641. Cousins in Binary Tree II

from utils import chunk, toTree, printTree
from typing import Optional
from classes import TreeNode
from collections import deque, defaultdict


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, None)])  # node, parent

        while queue:
            # siblingSum[parent] = sum values of nodes belonging to the same parent
            # then sum of all cousin values = levelSum - siblingSum[parent]
            siblingSum = defaultdict(int)
            levelSum = 0

            # calculate levelSum and siblingSum by rotating through all values in queue
            for _ in range(len(queue)):
                curr, parent = queue[0]
                levelSum += curr.val
                siblingSum[parent] += curr.val
                queue.rotate(1)

            # in-place modification of tree to obtain cousinSum
            for _ in range(len(queue)):
                curr, parent = queue.popleft()
                curr.val = levelSum - siblingSum[parent]

                if curr.left:
                    queue.append((curr.left, curr))
                if curr.right:
                    queue.append((curr.right, curr))

        return root


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [5, 4, 9, 1, 10, None, 7],
        [3, 1, 2],
        [5, 4, 9, 1, 10, 8, 7, 2, 3, 1, 6, 7, 9, 11, 13],
        [1]
    ]
    for puzzle in chunk(puzzles, testSize):
        printTree(Solution().replaceValueInTree(toTree(puzzle[0])))
        print()
