# 641. Design Circular Deque

from utils import chunk


class MyCircularDeque:

    def __init__(self, k: int):
        self.i = 0
        self.j = 0
        self.k = k
        self.size = 0
        self.deque = [-1] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.size > 0:
            self.i -= 1
            if self.i == -1:
                self.i = self.k - 1

        self.deque[self.i] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.size > 0:
            self.j += 1
            if self.j == self.k:
                self.j = 0

        self.deque[self.j] = value
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.deque[self.i] = -1
        self.size -= 1
        if self.size > 0:
            self.i += 1
            if self.i == self.k:
                self.i = 0

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.deque[self.j] = -1
        self.size -= 1
        if self.size > 0:
            self.j -= 1
            if self.j == -1:
                self.j = self.k - 1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.i]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.j]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


if __name__ == "__main__":
    puzzles = [
        # ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
        #     "getRear", "isFull", "deleteLast", "insertFront", "getFront"],
        # [[3], [1], [2], [3], [4], [], [], [], [4], []],
        # ["MyCircularDeque", "insertLast", "deleteFront", "insertLast", "insertLast", "insertLast",
        #     "getRear", "insertFront", "insertFront", "insertFront", "getFront", "getRear"],
        # [[5], [1], [], [1], [2], [3], [], [4], [5], [6], [], []]
        ["MyCircularDeque", "insertFront", "getFront", "isEmpty", "deleteFront", "insertLast",
            "getRear", "insertLast", "insertFront", "deleteLast", "insertLast", "isEmpty"],
        [[8], [5], [], [], [], [3], [], [7], [7], [], [4], []]
    ]
    for words, prefixes in chunk(puzzles, 2):
        obj = eval(words[0])(*prefixes[0])
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(*prefix))
        print()
