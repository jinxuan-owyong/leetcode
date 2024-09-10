# 2807. Insert Greatest Common Divisors in Linked List

import math
from typing import Optional
from classes import ListNode
from utils import chunk, toLinkedList, printLinkedList


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        while curr:
            insert = ListNode(math.gcd(prev.val, curr.val))
            prev.next, insert.next = insert, curr
            prev, curr = curr, curr.next
        return head


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [18, 6, 10, 3],
        [7],
        [3, 12],
        [3, 6, 9]
    ]
    for puzzle in chunk(puzzles, testSize):
        printLinkedList(Solution().insertGreatestCommonDivisors(
            toLinkedList(puzzle[0])))
