# 3561. Resulting String After Adjacent Removals

from utils import chunk

class Solution:
    def resultingString(self, s: str) -> str:
        def isAdjacent(a, b):
            if a == 'a' and b == 'z' or a == 'z' and b == 'a':
                return True
            return chr(ord(a)+1) == b or chr(ord(b)+1) == a
        
        # remove adjacent pair as soon as we find a matching pair
        # after all chars have been checked, the stack stores the result
        stack = []
        for c in s:
            if stack and isAdjacent(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
        
        
        
if __name__ == "__main__":
    testSize = 1
    puzzles = [
        "abc",
        "adcb",
        "zadb",
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().resultingString(*puzzle))
