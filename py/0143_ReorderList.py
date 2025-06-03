# 143. Reorder List

from typing import Optional
from classes import ListNode
from utils import toLinkedList, printLinkedList


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use fast and slow pointers to find the midpoint
        # fast is either tail or one after tail, slow is midpoint or right of mid
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the linked list starting at slow
        prev = None
        curr = slow  # mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        tail = prev

        # reversing the linked list yields the following:
        # if 2,4,6,8,    first = 2,4,6  second = 8,6
        # if 2,4,6,8,10, first = 2,4,6  second = 10,8,6
        # both linked lists point to the initital mid (slow) pointer
        # for the even case, we only want the first 2 values of first
        # both first and second advance equal number of times, and second becomes None after 2 advances, so exit if second is None
        # for the odd case, both will advance 3 times, ending up at 6 where first == second, so we stop
        # since we last assigned 8 from the second linked list, we are already pointing at the last value 6
        first, second = head, tail
        start = ListNode()
        while second and first != second:
            start.next = first
            start, first = start.next, first.next
            start.next = second
            start, second = start.next, second.next


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
