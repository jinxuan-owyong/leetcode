# 1381. Design a Stack With Increment Operation

from utils import chunk


class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.add = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.size:
            return
        self.stack.append(x)
        self.add.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        x, inc = self.stack.pop(), self.add.pop()
        if self.stack:
            self.add[-1] += inc
        return x + inc

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            if k > len(self.stack):
                self.add[-1] += val
            else:
                self.add[k - 1] += val


if __name__ == "__main__":
    puzzles = [
        ["CustomStack", "push", "push", "pop", "push", "push", "push",
            "increment", "increment", "pop", "pop", "pop", "pop"],
        [[3], [1], [2], [], [2], [3], [4], [5, 100], [2, 100], [], [], [], []]
    ]
    for words, prefixes in chunk(puzzles, 2):
        obj = eval(words[0])(*prefixes[0])
        for word, prefix in zip(words[1:], prefixes[1:]):
            print(getattr(obj, word)(*prefix))
        print()
