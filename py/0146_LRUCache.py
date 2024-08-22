# 146. LRU Cache

class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key, self.val, self.prev, self.next = key, val, prev, next


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def remove(self, node):
        if self.size == 1:
            self.head, self.tail = None, None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            left, right = node.prev, node.next
            left.next, right.prev = right, left
            node.prev, node.next = None, None

        self.size -= 1

    def insertAtHead(self, node):
        self.size += 1

        if not self.head:
            self.head, self.tail = node, node
            return

        self.head.prev, node.next = node, self.head
        self.head = node

    def moveToHead(self, node):
        self.remove(node)
        self.insertAtHead(node)

    def removeTail(self):
        temp = self.tail
        self.remove(self.tail)
        return temp


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.dll.moveToHead(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        insert = ListNode(key, value)
        # existing key
        if key in self.cache:
            self.dll.moveToHead(self.cache[key])
            self.cache[key].val = value
            return

        # has capacity to hold more keys
        # invalidate oldest key if full
        if len(self.cache) == self.capacity:
            tail = self.dll.removeTail()
            del self.cache[tail.key]

        # invalidate oldest key if full
        self.dll.insertAtHead(insert)
        self.cache[key] = insert


if __name__ == "__main__":
    puzzles = [
        (["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
         [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]),
        (["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
         [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]),
        (["LRUCache", "put", "put", "put", "put", "get", "get"],
         [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]),
        (["LRUCache", "put", "put", "get", "put", "put", "get"],
         [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]])
    ]
    for operations, params in puzzles:
        obj = LRUCache(*params[0])
        for op, param in zip(operations[1:], params[1:]):
            print(op, param)
            print(getattr(obj, op)(*param))
        print()
