# 206. Reverse Linked List

from typing import Optional
from classes import ListNode
from utils import chunk, toLinkedList, printLinkedList


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [1, 2, 3, 4, 5],
        [1, 2],
        []
    ]
    for puzzle in chunk(puzzles, testSize):
        printLinkedList(Solution().reverseList(toLinkedList(puzzle[0])))
