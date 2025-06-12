# 138. Copy List with Random Pointer

from utils import chunk
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copy = {None: None}  # edge case: a node can point to None

        # initialise copies of nodes
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next

        # then join them to the desired target
        # this cannot be done in one loop as we may try to point to an uninitialised node
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]

# class Solution:
#     def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
#         # values are not necessarily unique
#         # need to map the position of the original node to its index to identify which position it is pointing to
#         # first copy the values in sequence (next)
#         # then map the position of the random values to the new linked list
#         def copy(node, i):
#             if not node:
#                 return None
#             curr = Node(node.val)
#             nei = copy(node.next, i+1)
#             origPos[node] = i
#             copyNode[i] = curr
#             curr.next = nei
#             return curr

#         origPos = {}  # node pointer -> index
#         copyNode = {}  # index -> node pointer
#         randPos = {}  # points the ith node to the index of the random node
#         clone = copy(head, 0)

#         # identify the random index the current node is pointing to
#         curr = head
#         while curr:
#             if curr.random != None:
#                 randPos[origPos[curr]] = origPos[curr.random]
#             else:
#                 randPos[origPos[curr]] = -1
#             curr = curr.next

#         # map old random to new random based on the relationship identified in the above loop
#         i = 0
#         curr = clone
#         while curr:
#             if randPos[i] >= 0:
#                 curr.random = copyNode[randPos[i]]
#             else:
#                 curr.random = None
#             curr = curr.next
#             i += 1

#         return clone
