# 432. All O`one Data Structure

from utils import chunk


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.pointer = {}

    def swapNodes(self, left, right):
        if not left or not right:
            return
        # headSection <-> left <-> right <-> tailSection
        headSection, tailSection = left.prev, right.next
        left.prev, left.next = right, tailSection
        right.prev, right.next = headSection, left

        # edge case
        if headSection:
            headSection.next = right
        if tailSection:
            tailSection.prev = left

        # shifting results in change in head or tail
        if self.head.prev:
            self.head = self.head.prev
        if self.tail.next:
            self.tail = self.tail.next

    def shiftRight(self, val):
        curr = self.pointer[val]
        # headSection <-> left (curr) <-> right (curr.next) <-> tailSection
        self.swapNodes(curr, curr.next)

    def shiftLeft(self, val):
        curr = self.pointer[val]
        # headSection <-> left (curr.prev) <-> right (curr) <-> tailSection
        self.swapNodes(curr.prev, curr)

    def remove(self, val):
        if self.pointer[val] == self.head:
            # pop front
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            else:
                self.head.prev = None
        elif self.pointer[val] == self.tail:
            # pop back
            self.tail = self.tail.prev
            if self.size == 1:
                self.head = None
            else:
                self.tail.next = None
        else:
            curr = self.pointer[val]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.size -= 1

    def pushFront(self, val):
        self.size += 1
        if not self.head:
            self.head = self.tail = ListNode(val)
        else:
            self.head.prev = ListNode(val, None, self.head)
            self.head = self.head.prev

        self.pointer[val] = self.head


class AllOne:

    def __init__(self):
        self.count = {}
        self.order = LinkedList()  # count: smallest -> largest

    def inc(self, key: str) -> None:
        if key not in self.count:
            self.count[key] = 1
            self.order.pushFront(key)
        else:
            self.count[key] += 1
            while True:
                curr = self.order.pointer[key]
                # insertion results in out of order linked list
                if curr.next and self.count[curr.val] > self.count[curr.next.val]:
                    self.order.shiftRight(key)
                else:
                    break

    def dec(self, key: str) -> None:
        # if this is already the smallest key, it will be near the head, but not necessarily at the head
        if self.count[key] == 1:
            del self.count[key]
            self.order.remove(key)
        else:
            self.count[key] -= 1
            while True:
                curr = self.order.pointer[key]
                # insertion results in out of order linked list
                if curr.prev and self.count[curr.val] < self.count[curr.prev.val]:
                    self.order.shiftLeft(key)
                else:
                    break

    def getMaxKey(self) -> str:
        if self.order.size == 0:
            return ""
        return self.order.tail.val

    def getMinKey(self) -> str:
        if self.order.size == 0:
            return ""
        return self.order.head.val


if __name__ == "__main__":
    puzzles = [
        ["AllOne", "inc", "inc", "getMaxKey",
            "getMinKey", "inc", "getMaxKey", "getMinKey"],
        [[], ["hello"], ["hello"], [], [], ["leet"], [], []],
        ["AllOne", "inc", "inc", "inc", "inc", "getMaxKey",
            "getMinKey", "inc", "dec", "getMinKey"],
        [[], ["pear"], ["mango"],  ["banana"], [
            "mango"], [], [], ["orange"], ["banana"], []],
        ["AllOne", "inc", "inc", "inc", "inc", "getMaxKey", "getMinKey"],
        [[], ["banana"], ["pear"], ["mango"], ["mango"], [], []],
        ["AllOne", "inc", "inc", "inc", "inc", "inc",
            "inc", "dec", "getMaxKey", "getMinKey"],
        [[], ["banana"], ["banana"], ["mango"], ["mango"],
            ["pear"], ["pear"], ["banana"], [], []],
        ["AllOne", "inc", "inc", "getMaxKey", "getMinKey",
            "dec", "dec", "getMinKey", "inc", "getMinKey"],
        [[], ["hello"], ["hello"], [], [], ["hello"], ["hello"], [], ["hello"], []]
    ]
    for words, prefixes in chunk(puzzles, 2):
        obj = eval(words[0])(*prefixes[0])
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(*prefix))
        print("-----------------------------------------------------")
