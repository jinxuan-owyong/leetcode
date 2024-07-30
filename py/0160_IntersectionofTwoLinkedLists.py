# 160. Intersection of Two Linked Lists

from classes import ListNode
from utils import toLinkedList
from typing import Optional


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        # despite difference in lengths of a and b,
        # they will both traverse a + b nodes after 2 rounds
        # and traverse along the same path before they reach the end
        # 4 -> 1 -> (8) -> (4) -> (5) -> 5 -> 6 -> 1 -> (8) -> (4) -> (5)
        # 5 -> 6 -> 1 -> (8) -> (4) -> (5) -> 4 -> 1 -> (8) -> (4) -> (5)
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


if __name__ == "__main__":
    puzzles = [
        (8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3),
        (2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1)
    ]
    for intersectVal, listA, listB, skipA, skipB in puzzles:
        a, b = toLinkedList(listA), toLinkedList(listB)
        joinA, joinB = a, b
        for _ in range(skipA):
            joinA = joinA.next
        for _ in range(skipB - 1):
            joinB = joinB.next
        joinB.next = joinA

        result = Solution().getIntersectionNode(a, b)
        if result:
            print(result.val)
        else:
            print(None)

"""
Runtime
82
ms
Beats
52.36%
of users with Python3
Memory
27.04
MB
Beats
74.32%
of users with Python3
13
"""
