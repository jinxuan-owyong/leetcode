# 143. Reorder List

from typing import Optional
from classes import ListNode
from utils import toLinkedList, printLinkedList


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # even: right of middle
        mid = tail = head
        while tail and tail.next:
            mid = mid.next
            tail = tail.next.next

        # reverse LL until both point to the middle element
        curr = mid
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        tail = prev

        # 0 -> 0 -> 0 <- 0
        # ^head     ^mid ^tail
        while head != mid and tail != mid:
            temp = head.next
            head.next = tail
            temp2 = tail.next
            tail.next = temp
            head = temp
            tail = temp2


if __name__ == "__main__":
    puzzles = [
        [2, 4, 6, 8],
        [2, 4, 6, 8, 10],
        [1, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1]
    ]
    for puzzle in puzzles:
        ll = toLinkedList(puzzle)
        Solution().reorderList(ll)
        printLinkedList(ll)

"""
Runtime
46
ms
Beats
94.51%
Memory
24.60
MB
Beats
73.29%
"""
