# 23. Merge k Sorted Lists

from utils import chunk, toLinkedList, printLinkedList
from typing import Optional, List
from classes import ListNode
import heapq


class Solution:
    # divide and conquer approach to solve. if we have 4 lists, merge 2 first, then merge the resulting 2
    # this forms a binary tree of depth log k, and iterating through all nodes we have O(N * log k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1

            root = ListNode()
            curr = root
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next

            curr.next = list1 if list1 else list2
            return root.next

        def divide(i, j):
            if i == j:
                return lists[i]

            mid = i + (j-i)//2
            list1 = divide(i, mid)
            list2 = divide(mid+1, j)

            return merge2(list1, list2)

        if not lists:
            return None
        return divide(0, len(lists)-1)


# class ListNode2:
#     # add wrapper to implement < comparison for pq
#     def __init__(self, node):
#         self.node = node

#     def __lt__(self, other):
#         return self.node.val < other.node.val


# class Solution:
#     # use pq to identify the smallest node out of k
#     # each extract and insert operation is O(log k), repeat it 2N times to get O(N * log k)
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         pq = []
#         for node in lists:
#             if node:
#                 heapq.heappush(pq, ListNode2(node))

#         root = ListNode()
#         curr = root

#         while pq:
#             node = heapq.heappop(pq).node  # unwrap class
#             curr.next = ListNode(node.val)
#             curr = curr.next
#             if node.next:
#                 heapq.heappush(pq, ListNode2(node.next))

#         return root.next

# class Solution:
#     # brute force, O(N * k)
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         root = ListNode()
#         curr = root

#         while True:
#             minNode = ListNode(float('inf'))
#             minIdx = -1
#             # repeatedly find the smallest node so far
#             for i in range(len(lists)):
#                 if lists[i] and lists[i].val < minNode.val:
#                     minNode = lists[i]
#                     minIdx = i

#             if minIdx >= 0:
#                 curr.next = minNode
#                 curr = curr.next
#                 lists[minIdx] = lists[minIdx].next
#             else:
#                 break

#         return root.next


if __name__ == "__main__":
    testSize = 1
    puzzles = [
        [[1, 4, 5], [1, 3, 4], [2, 6]],
        [],
        [[]],
        [[], [1]],
    ]
    for puzzle in chunk(puzzles, testSize):
        lists = list(map(toLinkedList, puzzle[0]))
        printLinkedList(Solution().mergeKLists(lists))
