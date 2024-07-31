# 1105. Filling Bookcase Shelves


from typing import List


# https://www.youtube.com/watch?v=lFYPPPTp8qE
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}

        def fitBooksInRow(i: int) -> int:
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]

            rowHeight = 0
            remainingWidth = shelfWidth
            result = 1E10

            for j in range(i, len(books)):
                # not possible to fit anymore books in the row
                if remainingWidth < books[j][0]:
                    break

                remainingWidth -= books[j][0]
                rowHeight = max(rowHeight, books[j][1])
                # for each book[j] added to the current row
                # start a new row to compare whether the result is better
                result = min(result, fitBooksInRow(j + 1) + rowHeight)

            cache[i] = result
            return result

        return fitBooksInRow(0)


if __name__ == "__main__":
    puzzles = [
        ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4),
        ([[1, 3], [2, 4], [3, 2]], 6)
    ]
    for puzzle in puzzles:
        print(Solution().minHeightShelves(*puzzle))

"""
Runtime
47
ms
Beats
83.90%
Memory
17.04
MB
Beats
48.87%
"""
