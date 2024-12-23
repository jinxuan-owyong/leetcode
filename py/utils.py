from classes import Node, ListNode, TreeNode
from typing import Optional, List, Generator
from collections import deque


def chunk(original: List[int], size: int) -> Generator[List[int], None, None]:
    if len(original) % size != 0:
        raise ValueError("Input data length is invalid")
    rows = len(original) // size
    for i in range(rows):
        start = i * size
        yield original[start:start+size]


def toGraph(adjList: List) -> Node:
    nodes = [Node(i + 1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0] if nodes else None


def printGraph(s: Optional[Node]):
    if not s:
        print()
        return
    seen = set()
    frontier = deque()
    frontier.append(s)
    while frontier:
        curr: Node = frontier.popleft()
        if curr and curr.val in seen:
            continue
        seen.add(curr.val)
        frontier.extend(curr.neighbors)
        print(curr.val, [n.val for n in curr.neighbors])


def toLinkedList(nums: List[int]) -> ListNode:
    # returns the head
    prev = None
    for n in nums[::-1]:
        prev = ListNode(n, prev)
    return prev


def getNode(nums: Optional[ListNode], i: int) -> Optional[ListNode]:
    if i == -1:
        return None
    for _ in range(i):
        nums = nums.next
    return nums


def getTail(nums: Optional[ListNode]) -> Optional[ListNode]:
    while nums.next:
        nums = nums.next
    return nums


def printLinkedList(nums: Optional[ListNode]) -> None:
    while nums:
        print(nums.val, end=' ')
        nums = nums.next
    print()


def toTree(nodes: List[int]) -> Optional[TreeNode]:
    if (not nodes):
        return None
    nodes = [None if val == None else TreeNode(int(val)) for val in nodes]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def printTree(node: Optional[TreeNode]):
    if not node:
        return
    printTree(node.left)
    print(node.val, end=' ')
    printTree(node.right)
