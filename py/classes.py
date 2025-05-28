from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val: int = val
        self.neighbors: List[Node] = neighbors if neighbors is not None else []


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end