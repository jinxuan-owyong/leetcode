# 590. N-ary Tree Postorder Traversal

from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def traverse(node: 'Node'):
            if not node:
                return

            for child in node.children:
                traverse(child)

            result.append(node.val)

        traverse(root)
        return result
