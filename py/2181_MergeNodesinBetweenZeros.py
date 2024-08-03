# 2181. Merge Nodes in Between Zeros

from typing import Optional
from classes import ListNode
from utils import toLinkedList, printLinkedList


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        curr = head.next
        start = None

        while curr != None:
            if curr.val == 0:
                if not start:
                    start = ListNode(total)
                    result = start
                else:
                    start.next = ListNode(total, curr.next)
                    start = start.next

                total = 0

            else:
                total += curr.val

            curr = curr.next

        return result


if __name__ == "__main__":
    puzzles = [
        [0, 3, 1, 0, 4, 5, 2, 0],
        [0, 1, 0, 3, 0, 2, 2, 0]
    ]
    for puzzle in puzzles:
        printLinkedList(Solution().mergeNodes(toLinkedList(puzzle)))
