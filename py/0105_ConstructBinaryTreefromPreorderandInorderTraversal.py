# 105. Construct Binary Tree from Preorder and Inorder Traversal

from utils import chunk,  printTree
from typing import Optional, List
from classes import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder traversal gives us root, left, right. split preorder[1:] into
        2 equal halves to obtain preorder traversal of the left/right subtree
        we can obtain the values corresponding to the subtrees from the inorder traversal
        since all values to the left of the root belong to the left subtree
        """
        # can be improved to use indices instead of slicings
        def traverse(preo, ino):
            if not preo:
                return None

            i = ino.index(preo[0])
            inoLeft, inoRight = ino[:i], ino[i+1:]
            numLeft = len(inoLeft)
            preLeft, preRight = preo[1:numLeft+1], preo[numLeft+1:]

            return TreeNode(
                val=preo[0],
                left=traverse(preLeft, inoLeft),
                right=traverse(preRight, inoRight)
            )

        return traverse(preorder, inorder)


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3, 4],
        [2, 1, 3, 4],
        [3, 9, 20, 15, 7],
        [9, 3, 15, 20, 7],
        [-1],
        [-1],
    ]
    for puzzle in chunk(puzzles, testSize):
        printTree(Solution().buildTree(*puzzle))
        print()
