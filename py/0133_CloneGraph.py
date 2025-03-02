# 133. Clone Graph

from utils import chunk, toGraph, printGraph
from typing import Optional
from classes import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        # we need a reference to an existing node since
        # there can be multiple nodes pointing to the same node
        ref = {node.val: Node(node.val)}
        stack = [(node, ref[node.val])]
        while stack:
            src, dst = stack.pop()
            for nei in src.neighbors:
                if nei.val in ref:
                    dst.neighbors.append(ref[nei.val])
                    # stop exploring since we already visited this node
                else:
                    tmp = Node(nei.val)
                    dst.neighbors.append(tmp)
                    stack.append((nei, tmp))
                    ref[nei.val] = tmp

        return ref[node.val]


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[2, 4], [1, 3], [2, 4], [1, 3]],
        [[]],
        [],
    ]
    for puzzle in chunk(puzzles, testSize):
        clone = Solution().cloneGraph(toGraph(puzzle[0]))
        printGraph(clone)
        print()
