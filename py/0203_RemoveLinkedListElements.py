# 203. Remove Linked List Elements

from classes import ListNode
from utils import toLinkedList, printLinkedList
from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            if not head:
                return None
            elif head.val == val:
                head = head.next
                curr = head
            elif curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head


if __name__ == "__main__":
    puzzles = [
        ([1, 2, 6, 3, 4, 5, 6], 6),
        ([], 1),
        ([7, 7, 7, 7], 7),
        ([7], 3),
        [[7], 7]
    ]
    for puzzle in puzzles:
        printLinkedList(Solution().removeElements(
            toLinkedList(puzzle[0]), puzzle[1]))

"""
Runtime
48
ms
Beats
62.85%
of users with Python3
Memory
19.43
MB
Beats
56.52%
of users with Python3
5
"""
