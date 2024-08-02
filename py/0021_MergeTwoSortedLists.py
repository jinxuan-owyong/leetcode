# 21. Merge Two Sorted Lists

from typing import Optional
from classes import ListNode
from utils import toLinkedList, printLinkedList


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        head = curr = ListNode(-10000)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return head.next


if __name__ == "__main__":
    puzzles = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
        ([1, 3, 5, 7], [4, 6, 8, 10, 12])
    ]
    for a, b in puzzles:
        printLinkedList(Solution().mergeTwoLists(
            toLinkedList(a), toLinkedList(b)))

"""
Runtime
32
ms
Beats
90.15%
Memory
16.55
MB
Beats
27.14%
"""
