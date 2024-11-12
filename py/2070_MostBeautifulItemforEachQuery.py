# 2070. Most Beautiful Item for Each Query

from utils import chunk
from typing import List
import bisect


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        bestBeauty = {}
        for (p, b) in items:
            bestBeauty[p] = max(bestBeauty[p], b) if p in bestBeauty else b

        priceToBeauty = sorted(bestBeauty.items())
        # convert into a prefix max array
        best = priceToBeauty[0][1]
        for i, (p, b) in enumerate(priceToBeauty):
            if b > best:
                best = b
            priceToBeauty[i] = (p, best)

        minPrice, _ = priceToBeauty[0]

        result = [0] * len(queries)
        for i, q in enumerate(queries):
            if q < minPrice:
                result[i] = 0
            else:
                # bisect_left returns the index where priceToBeauty[i] > q if q does not exist
                # otherwise priceToBeauty[i] == q if it exists
                # this can lead to out of bounds, and we also want the first price that is <= q
                j = bisect.bisect_left(priceToBeauty, q, key=lambda x: x[0])
                if j == len(priceToBeauty) or priceToBeauty[j][0] > q:
                    j -= 1
                result[i] = priceToBeauty[j][1]

        return result


if __name__ == "__main__":
    testSize = 2
    puzzles = [
        [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]],
        [1, 2, 3, 4, 5, 6],
        [[1, 2], [1, 2], [1, 3], [1, 4]],
        [1],
        [[10, 1000]],
        [5],
        [[571, 936], [648, 906], [751, 308], [165, 256], [354, 606], [565, 560], [238, 764], [479, 351], [909, 267], [
            215, 902], [258, 698], [945, 805], [108, 363], [813, 591], [443, 262], [863, 255], [967, 935], [685, 582], [898, 138]],
        [269, 166, 617, 1169, 1637, 393, 201, 1182, 1404, 1313]
    ]
    for puzzle in chunk(puzzles, testSize):
        print(Solution().maximumBeauty(*puzzle))
