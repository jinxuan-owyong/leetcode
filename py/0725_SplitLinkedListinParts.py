# 725. Split Linked List in Parts

from utils import chunk, toLinkedList, printLinkedList
from typing import Optional, List
from classes import ListNode


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # get length of LL
        curr, size = head, 0
        while curr:
            curr = curr.next
            size += 1

        result = []
        # empty lists will be handled below
        numExtras = size % k if size > k else 0

        for _ in range(min(k, size)):
            prev, curr = None, head
            # when size <= k, we need to ensure minimum partLength 1
            # otherwise floor division yields 0
            partLength = size // k if size > k else 1

            # parts occurring earlier should always have a size
            # greater than or equal to parts occurring later
            if numExtras:
                partLength += 1
                numExtras -= 1

            # split LL
            for _ in range(partLength):
                prev = head
                head = head.next
            if prev:
                prev.next = None
            result.append(curr)

        if k > size:
            result.extend([None] * (k - size))

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [1, 2, 3],
        5,
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        3,
        [1, 2],
        1,
        [1, 2],
        2,
        [1, 2],
        3,
        [1, 2, 3, 4],
        5
    ]
    for puzzle in chunk(puzzles, testSize):
        result = Solution().splitListToParts(
            toLinkedList(puzzle[0]), puzzle[1])
        for ll in result:
            printLinkedList(ll)
        print('end')
