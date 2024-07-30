# 83. Remove Duplicates from Sorted List

from classes import ListNode
from utils import toLinkedList, printLinkedList
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


if __name__ == "__main__":
    puzzles = [
        [1, 1, 2],
        [1, 1, 2, 3, 3],
        [],
        [1],
        [1, 1, 1, 1, 1, 1]
    ]
    for puzzle in puzzles:
        printLinkedList(Solution().deleteDuplicates(toLinkedList(puzzle)))

"""
Runtime
42
ms
Beats
45.04%
of users with Python3
Memory
16.56
MB
Beats
64.12%
of users with Python3
6
"""
