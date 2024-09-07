# 1367. Linked List in Binary Tree

from utils import chunk, toLinkedList, toTree
from typing import Optional
from classes import ListNode, TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], curr: Optional[ListNode]) -> bool:
            if not curr:  # matched all elements in LL
                return True
            if not root:  # not enough elements in tree
                return False
            if root.val == curr.val:  # begin traversal
                if dfs(root.left, curr.next) or dfs(root.right, curr.next):
                    return True
                # try subtrees if false
            if curr != head:  # element in tree does not match LL, start from head
                return False
            # try traversing subtrees
            return dfs(root.left, head) or dfs(root.right, head)
        return dfs(root, head)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [4, 2, 8],
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
        [1, 4, 2, 6],
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
        [1, 4, 2, 6, 8],
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3],
        [2, 2, 1],
        [2, None, 2, None, 2, None, 1]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().isSubPath(toLinkedList(
            puzzle[0]), toTree(puzzle[1])))
