# 1405. Longest Happy String


from utils import chunk
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [
            *([(-a, 'a')] if a > 0 else []),
            *([(-b, 'b')] if b > 0 else []),
            *([(-c, 'c')] if c > 0 else [])
        ]
        heapq.heapify(maxHeap)

        result = []
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            count *= -1

            if count == 0:
                break

            # cannot extend with char at top of heap as string will have > 2 repeated characters
            # "cc", [(5, "c"), (1, "a"), (1, "b")]
            # "cca", [(5, "c"), (1, "b"), (0, "a")]
            # "ccacc", [(3, "c"), (1, "b"), (0, "a")]
            # "ccaccb", [(3, "c"), (0, "b"), (0, "a")]
            # "ccaccbcc", [(1, "c"), (0, "b"), (0, "a")]
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                if not maxHeap:
                    break

                # use the next valid char instead
                countNext, charNext = heapq.heappop(maxHeap)
                countNext *= -1

                result.append(charNext)
                countNext -= 1
                if countNext > 0:
                    heapq.heappush(maxHeap, (-countNext, charNext))
                heapq.heappush(maxHeap, (-count, char))
            else:
                result.append(char)
                count -= 1
                if count > 0:
                    heapq.heappush(maxHeap, (-count, char))

        return "".join(result)


if __name__ == "__main__":
    testSize = 3
    puzzles = [
        1, 1, 7,
        7, 1, 0,
        1, 0, 1,
        0, 5, 8,
        2, 10, 6
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().longestDiverseString(*puzzle))
