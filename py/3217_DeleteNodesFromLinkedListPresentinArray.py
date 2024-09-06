# 3217. Delete Nodes From Linked List Present in Array

from utils import chunk
from typing import Optional, List
from classes import ListNode
from utils import toLinkedList, printLinkedList


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        removable = set(nums)
        prev, curr = None, head
        while curr:
            skipped = False
            if curr.val in removable:
                if curr == head:
                    head = head.next
                else:
                    prev.next = curr.next
                    skipped = True
            # edge case: [1], [1, 1, 2, 2]
            if not skipped:
                prev = curr
            curr = curr.next
        return head


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3],
        toLinkedList([1, 2, 3, 4, 5]),
        [1],
        toLinkedList([1, 2, 1, 2, 1, 2]),
        [5],
        toLinkedList([1, 2, 3, 4]),
        [1],
        toLinkedList([1, 1, 1, 1, 2, 3, 4]),
        [2],
        toLinkedList([1, 1, 2, 2]),
        [1],
        toLinkedList([1]),
        [2],
        toLinkedList([1]),
        [1],
        toLinkedList([2]),
    ]
    for puzzle in chunk(puzzles, testSize):
        printLinkedList(Solution().modifiedList(*puzzle))
