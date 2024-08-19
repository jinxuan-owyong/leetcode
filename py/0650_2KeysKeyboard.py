# 650. 2 Keys Keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        def paste(curr: int, steps: int, clipboard: int) -> int:
            if curr > n:
                return 1E10
            if curr == n:
                return steps
            # either paste with current clipboard, or copy and paste
            return min(paste(curr + clipboard, steps + 1, clipboard), paste(curr + curr, steps + 2, curr))
        
        if n == 1:
            return 0

        return paste(1, 1, 1)


if __name__ == "__main__":
    puzzles = [
        *range(1, 20)
    ]
    for puzzle in puzzles:
        print(Solution().minSteps(puzzle))
