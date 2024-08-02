# 155. Min Stack

class MinStack:

    def __init__(self):
        self.minValues = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minValues:
            self.minValues.append(val)
        else:
            self.minValues.append(min(val, self.minValues[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minValues.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]


if __name__ == "__main__":
    puzzles = [
        (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
         [[], [-2], [0], [-3], [], [], [], []]),
        (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
         [[], [1], [2], [0], [], [], [], []])
    ]
    for operations, arguments in puzzles:
        obj = MinStack()
        for op, arg in zip(operations[1:], arguments[1:]):
            method = getattr(obj, op)
            if not arg:
                print(method())
            else:
                method(arg[0])

"""
Runtime
63
ms
Beats
19.01%
Memory
20.47
MB
Beats
62.33%
"""
