# 297. Serialize and Deserialize Binary Tree

from utils import chunk, toTree, isSameTree
from typing import Optional
from classes import TreeNode
from collections import deque


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # perform preorder traversal to extract values - O(N) space/time
        result = []
        def dfs(curr):
            if not curr:
                result.append('null')
                return
            result.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return ','.join(result)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        if data == 'null':
            return None
        
        def dfs(i):
            if i[0] == len(nodes) or nodes[i[0]] == 'null':
                # after a leaf node is found, we do not continue searching in this subtree
                i[0] += 1
                return None
            
            curr = TreeNode(int(nodes[i[0]]))
            # the tree is rebuilt in the way it was serialised, using preorder traversal - O(N) space/time
            i[0] += 1
            curr.left = dfs(i)
            curr.right = dfs(i)
            return curr
            
        return dfs([0])
            



if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, None, None, 4, 5],
        [],
        [1, 2, 3, None, None, 4, 5, 6, 7],
    ]
    for puzzle in chunk(puzzles, testSize):
        start = toTree(puzzle[0])
        s = Codec().serialize(start)
        end = Codec().deserialize(s)
        print(isSameTree(start, end))
