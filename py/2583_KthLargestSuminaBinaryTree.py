# 2583. Kth Largest Sum in a Binary Tree
# https://leetcode.com/discuss/topic/5949862/beats-9875-python-bfs-heap-simple-explanation/

from utils import chunk, toTree
from typing import Optional
from classes import TreeNode
from collections import deque
import heapq


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        pq = []

        while queue:
            level = 0

            # 102. Binary Tree Level Order Traversal
            for _ in range(len(queue)):
                curr = queue.popleft()
                level += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # 215. Kth Largest Element in an Array
            heapq.heappush(pq,  level)
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0] if len(pq) == k else -1


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [5, 8, 9, 2, 1, 3, 7, 4, 6],
        2,
        [1, 2, None, 3],
        1,
        [1, 2, 3],
        3
    ]
    for puzzle in chunk(puzzles, testSize):
        nodes, k = puzzle
        print(Solution().kthLargestLevelSum(toTree(nodes), k))
