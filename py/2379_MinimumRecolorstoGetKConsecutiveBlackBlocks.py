# 2379. Minimum Recolors to Get K Consecutive Black Blocks

from utils import chunk


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        using a fixed window size of k, the minimum recolours is the
        minimum number of white blocks in the window
        """
        # initialise window
        count = {"B": 0, "W": 0}
        for i in range(k):
            count[blocks[i]] += 1

        # s[i:j] is the current window
        # i: next char to be removed
        # j: next char to be added
        i = 0
        result = count["W"]

        while i+k < len(blocks):
            count[blocks[i]] -= 1
            count[blocks[i+k]] += 1
            i += 1
            result = min(result, count["W"])

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        "WBBWWBBWBW", 7,
        "WBWBBBW", 2,
        "WBB", 1,
        "W", 1,
        "B", 1,
        "WWBBBWBBBBBWWBWWWB", 16,
        "BWWWBB", 6,
        "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", 100
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().minimumRecolors(*puzzle))
